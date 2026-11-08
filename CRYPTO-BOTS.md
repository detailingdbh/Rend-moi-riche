# Les meilleurs bots de trading crypto sur GitHub 🤖

Comparatif établi à partir de la recherche GitHub et des README officiels de
chaque projet. Chiffres relevés le 8 novembre 2026.

> ⚠️ **Avant tout :** les étoiles mesurent la popularité, **pas les gains**.
> Aucun de ces bots n'est rentable tout seul : c'est **ta stratégie** qui
> gagne ou qui perd. Freqtrade le dit lui-même dans son README : *« Ne risquez
> pas d'argent que vous avez peur de perdre. »*

---

## Le verdict

| Ton profil | Le meilleur choix | Pourquoi |
|---|---|---|
| **Le meilleur bot en général** | **[Freqtrade](https://github.com/freqtrade/freqtrade)** | Le plus utilisé au monde, très bien entretenu, gratuit, mode simulation, interface web et Telegram. |
| Tu ne sais pas coder | [OctoBot](https://github.com/Drakkar-Software/OctoBot) | Interface visuelle, stratégies prêtes (Grid, DCA, TradingView, IA). |
| Tu codes en Python et veux des tests sérieux | [Jesse](https://github.com/jesse-ai/jesse) | Outils anti-chance : Monte Carlo, tests de significativité. |
| Tu veux faire du *market making* | [Hummingbot](https://github.com/hummingbot/hummingbot) | La référence, mais réservé aux utilisateurs avancés. |
| Tu es développeur expérimenté | [Nautilus Trader](https://github.com/nautechsystems/nautilus_trader) | Moteur de niveau professionnel (Rust + Python). |

---

## Le comparatif complet

| Bot | ⭐ Étoiles | Forks | Issues ouvertes | Dernière mise à jour | Licence | Langage |
|---|---|---|---|---|---|---|
| [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade) | **56,6 k** | 11,7 k | **25** | 07/11/2026 | GPL-3.0 | Python |
| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | 31,4 k | 4,2 k | 171 | 08/11/2026 | LGPL-3.0 | Rust / Python |
| [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | 21,1 k | 5,1 k | 204 | 06/11/2026 | Apache-2.0 | Python |
| [jesse-ai/jesse](https://github.com/jesse-ai/jesse) | 8,8 k | 1,3 k | **5** | 08/11/2026 | MIT | Python |
| [Drakkar-Software/OctoBot](https://github.com/Drakkar-Software/OctoBot) | 6,9 k | 1,3 k | 194 | 02/11/2026 | GPL-3.0 | Python |
| [Superalgos/Superalgos](https://github.com/Superalgos/Superalgos) | 5,8 k | 6 k | 108 | 07/11/2026 | Apache-2.0 | JavaScript |
| [enarjord/passivbot](https://github.com/enarjord/passivbot) | 2,2 k | 693 | 85 | 08/11/2026 | Unlicense | Python / Rust |

Le peu d'issues ouvertes chez Freqtrade (25 pour 56 000 étoiles) montre que
les bugs signalés sont traités vite : c'est un projet très bien entretenu.

### 🥇 Freqtrade — le meilleur choix

- **Simulation gratuite** (*dry-run*) : le bot tourne avec de l'argent fictif sur les vrais prix.
- **Backtesting** : teste ta stratégie sur les années passées.
- **Optimisation** automatique des paramètres, et **FreqAI** (apprentissage automatique) pour les stratégies adaptatives.
- **Interface web** (FreqUI) et **pilotage depuis Telegram** sur ton téléphone.
- Plateformes officiellement prises en charge, dont plusieurs **européennes** : Kraken, Bybit EU, MyOKX (OKX Europe), Gate EU, Binance, Bitget, Hyperliquid… Bitvavo et Kucoin sont validées par la communauté.
- Le dépôt [freqtrade-strategies](https://github.com/freqtrade/freqtrade-strategies) (5,6 k ⭐) propose des stratégies gratuites. Elles sont **« à but éducatif uniquement »** selon leurs auteurs : ce sont des exemples pour apprendre, pas des stratégies gagnantes clés en main.

### 🥈 OctoBot — le plus simple

- Interface graphique, sans code.
- Stratégies Grid, DCA, « paniers » de cryptos (comme un ETF), signaux TradingView, et mode IA (ChatGPT ou modèles locaux Ollama).
- Simulation et backtesting intégrés.
- Point faible : la nouvelle version (« node mode ») est **en bêta**, et le README prévient qu'elle peut avoir des bugs. 194 issues ouvertes.

### 🥉 Jesse — le plus rigoureux

- Syntaxe Python très simple pour écrire ses propres stratégies.
- Outils pour savoir si une stratégie gagne **par compétence ou par chance** : analyse Monte Carlo, tests de significativité des règles d'entrée.
- Seulement 5 issues ouvertes, licence MIT.

### Pour experts uniquement

- **Hummingbot** : *market making* et arbitrage. Il faut comprendre la tenue de carnet d'ordres.
- **Nautilus Trader** : moteur professionnel, pour développeurs expérimentés.
- **Passivbot** : il travaille **uniquement sur les contrats à terme perpétuels** (*futures*), donc avec **effet de levier**. On peut perdre plus vite que sa mise : à éviter quand on débute.

---

## 🚫 Les bots à éviter

**Projets abandonnés** : plus mis à jour, donc incompatibles avec les plateformes actuelles et sans correctifs de sécurité.

| Dépôt | Dernière mise à jour |
|---|---|
| askmike/gekko | février 2020 |
| CryptoSignal/Crypto-Signal | juillet 2024 |
| ctubio/Krypto-trading-bot | décembre 2024 |

**Les « sniper bots », « MEV bots » et « profit garanti »**. Pendant la
recherche, plusieurs dépôts différents de « Solana token sniper » avaient
**exactement la même description** et ont été mis à jour **le même jour**. C'est le
signe typique de copies créées en masse, souvent piégées pour voler la clé
privée de ton portefeuille. Ne lance jamais ce genre de code.

---

## Démarrer avec Freqtrade, sans risquer un euro

👉 **Guide d'installation complet, étape par étape : [INSTALLATION.md](INSTALLATION.md)**

Il faut [Docker](https://www.docker.com/products/docker-desktop/) installé sur
un ordinateur. Ces commandes viennent de la
[documentation officielle](https://www.freqtrade.io/en/stable/docker_quickstart/).

```bash
mkdir ft_userdata && cd ft_userdata
curl https://raw.githubusercontent.com/freqtrade/freqtrade/stable/docker-compose.yml -o docker-compose.yml
docker compose pull

# Crée les dossiers et la configuration.
# Réponds « oui » au mode dry-run et à FreqUI quand c'est demandé.
docker compose run --rm freqtrade create-userdir --userdir user_data
docker compose run --rm freqtrade new-config --config user_data/config.json
```

**Réponses conseillées aux questions de `new-config` :**

| Question | Réponse |
|---|---|
| Do you want to enable Dry-run (simulated trades)? | **Yes** (simulation, aucune clé d'API demandée) |
| Please insert your stake currency | `USDT` |
| Please insert your stake amount | `unlimited` (le capital fictif est réparti entre les trades) |
| Please insert max_open_trades | `3` |
| Time | *Have the strategy define timeframe.* |
| Please insert your display Currency | `EUR` |
| Select exchange | **binance** pour le test : son historique de prix public se télécharge vite, sans compte |
| Do you want to trade Perpetual Swaps? | **No** (pas d'effet de levier) |
| Do you want to enable Telegram? | No, pour l'instant |
| Do you want to enable the Rest API (includes FreqUI)? | **Yes**, puis choisis un identifiant et un mot de passe |

Kraken marche aussi, mais il ne fournit qu'un historique court : il faut
ajouter `--dl-trades` à `download-data`, et le téléchargement est beaucoup plus long.

**Étape obligatoire avant le backtest.** La configuration créée par défaut
choisit les cryptos selon le volume du moment (`VolumePairList`), et Freqtrade
refuse alors de lancer un backtest. Ouvre `user_data/config.json` et :

- dans le bloc `"exchange"`, remplace la liste vide `"pair_whitelist": [ ],` par une liste fixe de cryptos, dans la devise choisie (EUR ou USDT) :

  ```json
  "pair_whitelist": ["BTC/USDT", "ETH/USDT"],
  ```

- remplace tout le bloc `"pairlists": [ ... ]` par :

  ```json
  "pairlists": [{ "method": "StaticPairList" }],
  ```

Ensuite :

```bash
# Télécharge 90 jours de prix puis teste la stratégie d'exemple sur cette période
docker compose run --rm freqtrade download-data --config user_data/config.json --days 90 -t 5m
docker compose run --rm freqtrade backtesting --config user_data/config.json --strategy SampleStrategy -i 5m

# Lance le bot en simulation. L'interface web est sur http://localhost:8080
docker compose up -d
```

## Passer en argent réel

Le bot passe alors de vrais ordres avec ton argent. La documentation de
Freqtrade prévient : *« une mauvaise stratégie peut te faire perdre tout ton argent »*.

**0. Le backtest d'abord : 5 minutes, pas 4 semaines.** Le backtest n'est pas
une simulation qui dure : il rejoue en quelques minutes les **vrais prix des
derniers mois**. S'il montre une perte, lancer la même stratégie en réel, c'est
perdre de l'argent réel. `SampleStrategy` est un **exemple pédagogique**, pas une
stratégie conçue pour gagner.

**1. Ouvre un compte sur une plateforme autorisée en France** et prise en charge
par Freqtrade (par exemple Kraken, Bybit EU ou MyOKX). Vérifie son autorisation
sur le site de l'[AMF](https://www.amf-france.org/). Fais ton backtest sur
**cette même plateforme** (avec Kraken, ajoute `--dl-trades` à `download-data`).

**2. Dépose une petite somme**, que tu acceptes de perdre entièrement.

**3. Crée une clé d'API** sur la plateforme, avec ces réglages :
- ✅ trading au comptant (*spot*) uniquement ;
- ❌ **retraits désactivés**. Même si la clé est volée, personne ne peut sortir tes fonds ;
- ❌ pas de *futures* ni de marge ;
- si la plateforme le propose, limite la clé à l'adresse IP de la machine du bot.

**4. Mets tes clés dans un fichier à part**, `user_data/config-private.json`,
comme le recommande la documentation. Ne les montre à personne et ne les colle
jamais dans une conversation, même avec une IA.

```json
{
    "dry_run": false,
    "exchange": {
        "name": "kraken",
        "api_key": "TA_CLE_ICI",
        "secret": "TON_SECRET_ICI"
    }
}
```

Mets le nom de ta plateforme dans `"name"` (`kraken`, `okx`, `bybit`…) et une
devise qu'elle propose dans `"pair_whitelist"` (par exemple `BTC/EUR` sur Kraken).
N'ajoute pas de `db_url` : Freqtrade utilise alors automatiquement une base de
données séparée pour le réel, et tes trades de test ne se mélangent pas avec les vrais.

**5. Lance le bot en réel**

```bash
freqtrade trade --config user_data/config.json --config user_data/config-private.json --strategy SampleStrategy
```

**6. Le bot doit tourner jour et nuit.** Si l'ordinateur s'éteint, le bot
s'arrête, mais les positions ouvertes restent sur la plateforme. Un petit
serveur loué (VPS, quelques euros par mois) règle ce problème et donne une
adresse IP fixe pour l'étape 3. Pour tout revendre, utilise le bouton
*Force exit* dans FreqUI.

### Les règles d'or avant de passer à l'argent réel

1. **Un backtest positif, au minimum.** Idéalement, ajoute quelques semaines de simulation : si les résultats en direct sont bien moins bons que le backtest, la stratégie est sur-optimisée et perdra en réel.
2. **Petite somme d'abord**, uniquement de l'argent que tu acceptes de perdre entièrement.
3. **Clé d'API sans droit de retrait**, et limitée à l'adresse IP de ton serveur si la plateforme le permet.
4. **Toujours un stop-loss**, et **pas d'effet de levier** au début.
5. Vérifie que la plateforme est **autorisée en France** (liste blanche de l'[AMF](https://www.amf-france.org/)).
6. **Impôts :** les plus-values sont imposables, et les comptes ouverts sur des plateformes étrangères doivent être déclarés chaque année (formulaire 3916-bis).

### Et Revolut X ?

La bibliothèque [CCXT](https://github.com/ccxt/ccxt), que Freqtrade et OctoBot
utilisent pour parler aux plateformes, **prend en charge Revolut X** : prix,
historique, solde, passage et annulation d'ordres. En revanche, Revolut X ne
figure **pas** dans la liste officielle de Freqtrade, qui précise que les
autres plateformes CCXT *« peuvent fonctionner, sans garantie »*. Pour
démarrer, une plateforme officiellement prise en charge (Kraken, Bybit EU,
MyOKX…) est donc plus sûre.

---

## Faire tourner plusieurs bots

**Avec Freqtrade** ([documentation](https://www.freqtrade.io/en/stable/advanced-setup/)),
chaque bot a besoin de :
- son **propre fichier de configuration** (et souvent sa propre stratégie) ;
- sa **propre base de données** : `--db-url sqlite:///user_data/bot1.live.sqlite` ;
- son **propre port** pour l'interface web (8080, 8081, 8082…) ;
- son **propre bot Telegram**, si tu utilises Telegram.

[FreqUI](https://www.freqtrade.io/en/stable/freq-ui/) affiche ensuite tous les bots sur un même tableau de bord.

⚠️ Des bots branchés sur **le même compte** ne savent pas ce que font les
autres. Avec `"stake_amount": "unlimited"`, ils se disputent le même solde.
Donne à chaque bot un **montant fixe** (par exemple `"stake_amount": 20`), ou
utilise un **sous-compte** par bot si ta plateforme le permet.

**Avec OctoBot**, une seule installation (« node mode ») gère plusieurs
automatisations (Grid, DCA, TradingView…). **Avec Hummingbot**, le
[Dashboard](https://github.com/hummingbot/dashboard) crée, teste et pilote plusieurs bots.

---

## Tous les liens utiles

Liens officiels, **sans lien de parrainage**.

| Usage | Lien |
|---|---|
| Freqtrade (code) | https://github.com/freqtrade/freqtrade |
| Freqtrade (documentation) | https://www.freqtrade.io/en/stable/ |
| Freqtrade (stratégies gratuites) | https://github.com/freqtrade/freqtrade-strategies |
| OctoBot | https://github.com/Drakkar-Software/OctoBot · https://www.octobot.cloud/ |
| Jesse | https://github.com/jesse-ai/jesse · https://jesse.trade/ |
| Hummingbot | https://github.com/hummingbot/hummingbot · https://hummingbot.org/ |
| Docker | https://www.docker.com/products/docker-desktop/ |
| Créer un bot Telegram | https://t.me/BotFather |
| Plateformes de la liste officielle de Freqtrade | https://www.kraken.com/ · https://www.bybit.eu/ · https://www.okx.com/ · https://www.gate.com/en-eu · https://bitvavo.com/ |
| Vérifier une plateforme (France) | https://www.amf-france.org/fr/espace-epargnants/proteger-son-epargne/listes-blanches |
| Vérifier une plateforme (Europe, MiCA) | https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica |
