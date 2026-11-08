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

### Les règles d'or avant de passer à l'argent réel

1. **Au moins 4 semaines en simulation.** Si les résultats en direct sont bien moins bons que le backtest, la stratégie est sur-optimisée : ne la lance pas en réel.
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
