"""Machine à remonter le temps : que seraient devenus 54 € avec différentes méthodes ?

Données : bougies Binance BTC/USDT et ETH/USDT (dépôt NostalgiaForInfinityData)
jusqu'au 1er octobre 2026, complétées par CoinGecko jusqu'au 10 novembre 2026.
Frais : 0,6 % par achat ou vente (Coinbase Advanced, tarif « taker » petit volume).
Le taux euro/dollar est supposé constant : les résultats sont des pourcentages
appliqués à 54 €.
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(sys.argv[1])          # dossier binance/ des données (non fiables : lues comme données)
CG = Path(sys.argv[2])            # JSON CoinGecko
OUT = Path(sys.argv[3])           # résultats JSON

CAPITAL = 54.0
FEE = 0.006
W_BTC, W_ETH = 0.75, 0.25


def load(name):
    d = pd.read_feather(DATA / f"{name}.feather")
    d["date"] = pd.to_datetime(d["date"], utc=True)
    return d.set_index("date").sort_index()


def daily_closes():
    btc = load("BTC_USDT-1d")["close"]
    eth = load("ETH_USDT-1d")["close"]
    df = pd.DataFrame({"btc": btc, "eth": eth})
    df.index = df.index.normalize()
    cg = json.loads(CG.read_text())
    n = len(cg["bitcoin"])
    ts = np.linspace(cg["startTs"], cg["endTs"], n)
    cgdf = pd.DataFrame({"btc": cg["bitcoin"], "eth": cg["ethereum"]},
                        index=pd.to_datetime(ts, unit="ms", utc=True))
    cg_daily = cgdf.groupby(cgdf.index.normalize()).last()
    overlap = cg_daily.loc[cg_daily.index.isin(df.index)]
    check = {}
    if len(overlap):
        both = df.loc[overlap.index]
        check = {"jours_communs": int(len(overlap)),
                 "ecart_moyen_btc_pct": round(float(((overlap["btc"] / both["btc"]) - 1).abs().mean() * 100), 2)}
    extra = cg_daily.loc[cg_daily.index > df.index.max()]
    full = pd.concat([df, extra]).sort_index()
    return full, check


def drawdown(eq):
    peak = eq.cummax()
    dd = eq / peak - 1
    i = dd.idxmin()
    return float(dd.min()), i


def summarize(name, eq, extra=None):
    mdd, when = drawdown(eq)
    peak_before = eq.loc[:when].max()
    r = {
        "nom": name,
        "final": round(float(eq.iloc[-1]), 2),
        "gain": round(float(eq.iloc[-1] - CAPITAL), 2),
        "gain_pct": round(float(eq.iloc[-1] / CAPITAL - 1) * 100, 1),
        "pire_baisse_pct": round(mdd * 100, 1),
        "pire_baisse_eur": round(float(eq.loc[when] - peak_before), 2),
        "plus_bas": round(float(eq.min()), 2),
        "date_pire": when.strftime("%Y-%m-%d"),
    }
    if extra:
        r.update(extra)
    return r


def hold(px, w):
    """Achat au premier jour, rien d'autre."""
    p0 = px.iloc[0]
    units = {k: CAPITAL * wk * (1 - FEE) / p0[k] for k, wk in w.items()}
    return sum(units[k] * px[k] for k in units)


def basket_rebalanced(px, w):
    """Panier rééquilibré au début de chaque mois (comme un panier OctoBot)."""
    p0 = px.iloc[0]
    units = {k: CAPITAL * wk * (1 - FEE) / p0[k] for k, wk in w.items()}
    eq, last_month, fees = [], px.index[0].month, 0.0
    for t, row in px.iterrows():
        if t.month != last_month:
            last_month = t.month
            val = sum(units[k] * row[k] for k in units)
            for k, wk in w.items():
                target = val * wk
                cur = units[k] * row[k]
                diff = target - cur
                cost = abs(diff) * FEE
                fees += cost
                units[k] = (cur + diff - cost) / row[k]
        eq.append(sum(units[k] * row[k] for k in units))
    return pd.Series(eq, index=px.index), fees


def dca(px, w, months=6):
    """54 € découpés en 6 achats mensuels de 9 €, puis on garde."""
    part = CAPITAL / months
    units = {k: 0.0 for k in w}
    cash, done, last_month, eq = CAPITAL, 0, None, []
    for t, row in px.iterrows():
        if done < months and t.month != last_month:
            last_month = t.month
            for k, wk in w.items():
                units[k] += part * wk * (1 - FEE) / row[k]
            cash -= part
            done += 1
        eq.append(cash + sum(units[k] * row[k] for k in units))
    return pd.Series(eq, index=px.index)


def trend_sma(btc_full, start, end, n=50):
    """Bitcoin quand le prix est au-dessus de sa moyenne 50 jours, sinon en euros.
    Signal à la clôture d'un jour, exécution à la clôture du jour suivant."""
    sma = btc_full.rolling(n).mean()
    sig = (btc_full > sma).shift(1).fillna(False)
    px = btc_full.loc[start:end]
    sig = sig.loc[start:end]
    cash, units, eq, trades = CAPITAL, 0.0, [], 0
    for t in px.index:
        p = px.loc[t]
        if sig.loc[t] and units == 0 and cash > 0:
            units, cash, trades = cash * (1 - FEE) / p, 0.0, trades + 1
        elif not sig.loc[t] and units > 0:
            cash, units, trades = units * p * (1 - FEE), 0.0, trades + 1
        eq.append(cash + units * p)
    return pd.Series(eq, index=px.index), trades


def rsi(close, n=14):
    delta = close.diff()
    up = delta.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    down = (-delta.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    rs = up / down
    return 100 - 100 / (1 + rs)


def rsi_engulfing(c4, start, end):
    """Les règles de la vidéo : RSI < 30 + bougie englobante haussière (4 h),
    stop sous le plus bas, objectif 2R. Tout le capital, sans levier."""
    c4 = c4.copy()
    c4["rsi"] = rsi(c4["close"])
    o, h, l, c = c4["open"], c4["high"], c4["low"], c4["close"]
    engulf = (c.shift(1) < o.shift(1)) & (c > o) & (o <= c.shift(1)) & (c >= o.shift(1))
    signal = engulf & (np.minimum(c4["rsi"], c4["rsi"].shift(1)) < 30)
    d = c4.loc[start:end]
    sigs = signal.loc[start:end]
    cash, eq, idx, trades = CAPITAL, [], [], []
    pos = None
    for t, row in d.iterrows():
        if pos is None and sigs.loc[t]:
            entry = row["close"]
            stop = min(row["low"], d["low"].shift(1).get(t, row["low"]))
            if stop < entry:
                risk = entry - stop
                pos = {"entry": entry, "stop": stop, "target": entry + 2 * risk,
                       "units": cash * (1 - FEE) / entry, "t": t}
                cash = 0.0
        elif pos is not None:
            exit_px = None
            if row["low"] <= pos["stop"]:          # prudence : le stop passe en premier
                exit_px = pos["stop"]
            elif row["high"] >= pos["target"]:
                exit_px = pos["target"]
            if exit_px is not None:
                cash = pos["units"] * exit_px * (1 - FEE)
                trades.append({"entree": pos["t"].strftime("%Y-%m-%d %H:%M"),
                               "gagnant": bool(exit_px > pos["entry"])})
                pos = None
        val = cash if pos is None else pos["units"] * row["close"]
        eq.append(val)
        idx.append(t)
    eq = pd.Series(eq, index=pd.DatetimeIndex(idx))
    daily = eq.groupby(eq.index.normalize()).last()
    wins = sum(tr["gagnant"] for tr in trades)
    return daily, {"trades": len(trades), "gagnants": wins, "perdants": len(trades) - wins,
                   "reussite_pct": round(100 * wins / len(trades), 1) if trades else None}


def leverage_x10(h1, liq=0.10, horizons=(1, 7, 30)):
    """Long ×10 sur Bitcoin : liquidé si le prix baisse d'environ 10 % après l'entrée.
    Une entrée par jour à minuit (UTC)."""
    lows = h1["low"]
    opens = h1["open"]
    starts = [t for t in h1.index if t.hour == 0]
    res = {}
    for hz in horizons:
        hits, total = 0, 0
        for t in starts:
            endt = t + pd.Timedelta(days=hz)
            if endt > h1.index[-1]:
                break
            window = lows.loc[t:endt]
            total += 1
            if window.min() <= opens.loc[t] * (1 - liq):
                hits += 1
        res[f"{hz}j"] = {"entrees": total, "liquidees": hits,
                         "pct": round(100 * hits / total, 1) if total else None}
    t0 = h1.index[0]
    p0 = opens.iloc[0]
    hit = lows[lows <= p0 * (1 - liq)]
    res["depuis_le_debut"] = {"entree": t0.strftime("%Y-%m-%d"), "prix": round(float(p0)),
                              "liquide_le": hit.index[0].strftime("%Y-%m-%d") if len(hit) else None,
                              "jours": int((hit.index[0] - t0).days) if len(hit) else None}
    return res


def run_period(px_all, c4, label, start, end):
    px = px_all.loc[start:end]
    out = {"periode": label, "debut": px.index[0].strftime("%Y-%m-%d"),
           "fin": px.index[-1].strftime("%Y-%m-%d"), "methodes": [], "courbes": {}}
    w = {"btc": W_BTC, "eth": W_ETH}
    curves = {}
    eq_b, fees_b = basket_rebalanced(px, w)
    curves["big_crypto"] = (eq_b, summarize("Panier Big crypto (¾ Bitcoin, ¼ Ethereum)", eq_b,
                                           {"frais_reequilibrage": round(fees_b, 2)}))
    eq = hold(px, {"btc": 1.0})
    curves["btc"] = (eq, summarize("Bitcoin seul, gardé", eq))
    eq = hold(px, {"eth": 1.0})
    curves["eth"] = (eq, summarize("Ethereum seul, gardé", eq))
    eq = dca(px, w)
    curves["dca"] = (eq, summarize("Achats réguliers : 6 × 9 € (DCA)", eq))
    eq, n = trend_sma(px_all["btc"], start, end)
    curves["tendance"] = (eq, summarize("Bot « tendance » : Bitcoin au-dessus de sa moyenne 50 jours", eq,
                                       {"trades": n}))
    c4_end = min(pd.Timestamp(end), c4.index[-1])
    eq, stats = rsi_engulfing(c4, start, c4_end)
    curves["rsi_video"] = (eq, summarize("Bot de la vidéo : RSI < 30 + englobante, objectif 2R (4 h)", eq,
                                        {**stats, "fin_donnees": c4_end.strftime("%Y-%m-%d")}))
    for key, (eq, s) in curves.items():
        s["cle"] = key
        out["methodes"].append(s)
        out["courbes"][key] = {"dates": [d.strftime("%Y-%m-%d") for d in eq.index],
                               "valeurs": [round(float(v), 2) for v in eq.values]}
    return out


def main():
    px, check = daily_closes()
    c4 = load("BTC_USDT-4h")
    h1 = load("BTC_USDT-1h")
    end = px.index.max()
    res = {
        "capital": CAPITAL, "frais_pct": FEE * 100, "poids": {"btc": W_BTC, "eth": W_ETH},
        "controle_donnees": check, "derniere_date": end.strftime("%Y-%m-%d"),
        "prix_debut": {"btc": round(float(px["btc"].iloc[0])), "eth": round(float(px["eth"].iloc[0]))},
        "prix_fin": {"btc": round(float(px["btc"].iloc[-1])), "eth": round(float(px["eth"].iloc[-1]))},
        "periodes": [
            run_period(px, c4, "Depuis le 1er janvier 2024", px.index.min(), end),
            run_period(px, c4, "Les 12 derniers mois", end - pd.Timedelta(days=365), end),
        ],
        "levier_x10": leverage_x10(h1),
    }
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1))
    for p in res["periodes"]:
        print(f"\n== {p['periode']} ({p['debut']} -> {p['fin']})")
        for m in p["methodes"]:
            extra = ""
            if "trades" in m:
                extra = f" | trades {m['trades']}"
            if m.get("reussite_pct") is not None:
                extra += f" ({m['gagnants']} G / {m['perdants']} P, {m['reussite_pct']} %) fin {m['fin_donnees']}"
            print(f"{m['nom'][:62]:62s} {m['final']:7.2f} € ({m['gain_pct']:+6.1f} %) "
                  f"pire {m['pire_baisse_pct']:6.1f} % ({m['pire_baisse_eur']:+.2f} €, {m['date_pire']}) plus bas {m['plus_bas']}{extra}")
    print("\nlevier x10:", json.dumps(res["levier_x10"], ensure_ascii=False))
    print("controle:", check, "| prix début", res["prix_debut"], "fin", res["prix_fin"])


if __name__ == "__main__":
    main()
