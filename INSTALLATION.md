# Installer Freqtrade pas à pas 🛠️

Guide pour débutant, sur Windows, Mac ou serveur Linux.
Les commandes Docker viennent de la [documentation officielle](https://www.freqtrade.io/en/stable/docker_quickstart/).
Les étapes de configuration ont été testées avec **Freqtrade 2026.10**.

---

## 📱 Tu n'as qu'un iPhone ?

Freqtrade ne s'installe pas sur un téléphone. Trois solutions, de la plus simple à la plus complète :

| Solution | Difficulté | Coût | Plusieurs bots |
|---|---|---|---|
| **Bot intégré à une plateforme**, directement dans son app (ex. bots *Spot Grid* et *Spot DCA* d'OKX Europe) | ⭐ Très facile | Gratuit, seuls les frais de trading s'appliquent | Oui |
| **OctoBot Cloud** (le projet GitHub OctoBot, hébergé pour toi) + [app iPhone](https://apps.apple.com/us/app/octobot-crypto-investment/id6502774175) | ⭐⭐ Facile | Offre gratuite limitée ; environ 10 $/mois pour 10 bots, 30 $/mois pour 30 bots (prix relevés dans des avis, à vérifier sur le site officiel) | Oui |
| **Freqtrade sur un serveur loué**, piloté depuis l'iPhone | ⭐⭐⭐ Difficile sur téléphone | Serveur : quelques € par mois | Oui |

Dans tous les cas, vérifie d'abord que la plateforme est autorisée en France
([liste blanche de l'AMF](https://www.amf-france.org/fr/espace-epargnants/proteger-son-epargne/listes-blanches)).

### Freqtrade depuis un iPhone

1. **Loue un serveur Linux** (VPS) avec **Ubuntu** et **au moins 2 Go de mémoire**,
   par exemple chez [OVHcloud](https://www.ovhcloud.com/fr/vps/) ou [Hetzner](https://www.hetzner.com/cloud).
   Tu reçois par e-mail son **adresse IP** et son **mot de passe**.
2. **Installe l'app [Termius](https://apps.apple.com/fr/app/termius-modern-ssh-client/id549039908)**
   (gratuite). Ajoute un serveur (*New Host*) : l'adresse IP, l'utilisateur `root`
   et le mot de passe reçu. Connecte-toi.
3. **Suis ce guide en version « Serveur Linux »** à partir de l'étape 1. Pour chaque
   commande, ouvre ce guide sur GitHub dans Safari, copie, puis colle dans Termius.
   La barre au-dessus du clavier de Termius contient la touche **Ctrl** pour `nano`.
4. **À l'étape 4, réponds Yes à Telegram**, pour piloter le bot depuis ton iPhone :
   - le *token* : crée ton bot avec [@BotFather](https://t.me/BotFather) (commande `/newbot`) ;
   - le *chat id* : envoie un message à [@userinfobot](https://t.me/userinfobot), il te donne ton « Id » ;
   - ouvre ensuite la conversation avec ton bot et appuie sur **Démarrer** (*Start*).

   Tu pourras alors taper `/status`, `/profit`, `/balance` ou `/stop` dans Telegram.

---

## Où l'installer ?

| Pour… | Où | Pourquoi |
|---|---|---|
| Tester (backtest, simulation) | **Ton ordinateur** (Windows ou Mac) | Gratuit, rien à louer. |
| Trader en **argent réel** | **Un serveur Linux loué** (VPS, quelques € par mois) | Le bot doit tourner jour et nuit. Freqtrade **déconseille Docker sur Windows** pour l'argent réel : l'horloge se décale et des ordres peuvent être refusés. |

Tu peux commencer sur ton ordinateur puis tout recopier sur un serveur plus tard.

---

## Étape 1 — Installer Docker

Docker est le logiciel qui fait tourner Freqtrade sans rien installer d'autre.

- **Windows** : télécharge [Docker Desktop](https://www.docker.com/products/docker-desktop/), installe-le, puis **redémarre l'ordinateur**. La documentation de Freqtrade insiste : sans redémarrage, il peut y avoir des problèmes de réseau.
- **Mac** : télécharge [Docker Desktop](https://www.docker.com/products/docker-desktop/) et installe-le.
- **Serveur Linux** : connecte-toi au serveur, puis tape :
  ```bash
  curl -fsSL https://get.docker.com | sh
  ```

Sur Windows et Mac, **ouvre Docker Desktop** et attends qu'il indique que le moteur tourne (*Engine running*).
Garde-le ouvert pendant toutes les étapes.

## Étape 2 — Ouvrir un terminal

- **Windows** : menu Démarrer → tape `PowerShell` → ouvre-le.
- **Mac** : Spotlight (⌘ + Espace) → tape `Terminal` → ouvre-le.
- **Serveur Linux** : tu y es déjà, après ta connexion (`ssh`).

Copie-colle chaque commande ci-dessous, puis appuie sur **Entrée**.

## Étape 3 — Télécharger Freqtrade

```bash
mkdir ft_userdata
cd ft_userdata
curl https://raw.githubusercontent.com/freqtrade/freqtrade/stable/docker-compose.yml -o docker-compose.yml
docker compose pull
```

> **Windows** : écris `curl.exe` au lieu de `curl` dans la 3ᵉ commande. Dans
> PowerShell, `curl` tout court n'est pas le vrai curl, et la commande échoue.

Le téléchargement de `docker compose pull` prend quelques minutes.

## Étape 4 — Créer ta configuration

```bash
docker compose run --rm freqtrade create-userdir --userdir user_data
docker compose run --rm freqtrade new-config --config user_data/config.json
```

Freqtrade pose alors des questions. Réponds avec les flèches et **Entrée** :

| Question | Réponse |
|---|---|
| Do you want to enable Dry-run (simulated trades)? | **Yes** |
| Please insert your stake currency | `USDT` |
| Please insert your stake amount | `unlimited` |
| Please insert max_open_trades | `3` |
| Time | *Have the strategy define timeframe.* |
| Please insert your display Currency | `EUR` |
| Select exchange | **binance** (pour les tests : historique public, sans compte) |
| Do you want to trade Perpetual Swaps? | **No** |
| Do you want to enable Telegram? | No |
| Do you want to enable the Rest API (includes FreqUI)? | **Yes** |
| Adresse d'écoute (*listen address*) | laisse la valeur proposée et appuie sur Entrée |
| Username / Password | choisis un identifiant et un mot de passe pour l'interface web |

## Étape 5 — Fixer la liste des cryptos (obligatoire)

La configuration par défaut choisit les cryptos selon le volume du moment, et
Freqtrade refuse alors de faire un backtest. Cette commande fixe la liste à
Bitcoin et Ethereum. Copie-la en entier :

```bash
docker compose run --rm --entrypoint python freqtrade -c "import json;p='user_data/config.json';c=json.load(open(p));c['exchange']['pair_whitelist']=['BTC/USDT','ETH/USDT'];c['pairlists']=[{'method':'StaticPairList'}];json.dump(c,open(p,'w'),indent=4)"
```

Elle n'affiche rien si tout s'est bien passé.

## Étape 6 — Tester sur les 3 derniers mois (backtest)

```bash
docker compose run --rm freqtrade download-data --config user_data/config.json --days 90 -t 5m
docker compose run --rm freqtrade backtesting --config user_data/config.json --strategy SampleStrategy -i 5m
```

Un tableau de résultats s'affiche. Regarde surtout le **profit total** et la
**perte maximale** (*Max Drawdown*).

## Étape 7 — Lancer le bot en simulation

```bash
docker compose up -d
```

Ouvre **http://localhost:8080** dans ton navigateur et connecte-toi avec
l'identifiant de l'étape 4.

---

## Étape 8 — Passer en argent réel

À faire seulement si le backtest est positif. Tu dois aussi avoir lu les
règles de sécurité de [CRYPTO-BOTS.md](CRYPTO-BOTS.md#passer-en-argent-réel) :
plateforme autorisée, petite somme, clé d'API **sans droit de retrait**.

**8.1 — Créer le fichier de tes clés**

```bash
docker compose run --rm --entrypoint python freqtrade -c "import json;json.dump({'dry_run':False,'stake_currency':'EUR','exchange':{'name':'kraken','api_key':'COLLE_TA_CLE_ICI','secret':'COLLE_TON_SECRET_ICI','pair_whitelist':['BTC/EUR','ETH/EUR']}},open('user_data/config-private.json','w'),indent=4)"
```

Ce fichier est prévu pour **Kraken** avec un solde en **euros**. Pour une autre
plateforme, remplace `kraken` par son nom (`okx`, `bybit`…).

**8.2 — Coller tes clés dans le fichier**

- **Windows** : `notepad user_data\config-private.json`
- **Mac / Linux** : `nano user_data/config-private.json`. Pour enregistrer : Ctrl + O, Entrée. Pour quitter : Ctrl + X.

Remplace `COLLE_TA_CLE_ICI` et `COLLE_TON_SECRET_ICI` par ta clé et ton secret,
**en gardant les guillemets**. Ne montre ce fichier à personne.

**8.3 — Dire à Docker d'utiliser tes clés**

Ouvre `docker-compose.yml` (`notepad docker-compose.yml` ou `nano docker-compose.yml`).
Remplace les lignes sous `command: >` par celles-ci, **en gardant les espaces au
début des lignes** :

```yaml
    command: >
      trade
      --logfile /freqtrade/user_data/logs/freqtrade.log
      --db-url sqlite:////freqtrade/user_data/tradesv3.live.sqlite
      --config /freqtrade/user_data/config.json
      --config /freqtrade/user_data/config-private.json
      --strategy SampleStrategy
```

La base de données change de nom (`tradesv3.live.sqlite`) pour que les trades
simulés ne se mélangent pas avec les vrais, comme le recommande la documentation.

**8.4 — Relancer en réel**

```bash
docker compose down
docker compose up -d
docker compose logs -f
```

Dans les messages qui défilent, cherche la ligne **`Dry run is disabled`** :
elle confirme que le bot trade en réel. Si tu lis `Dry run is enabled`, il est
encore en simulation. Ctrl + C ferme l'affichage des messages, sans arrêter le bot.

---

## Commandes utiles

| Pour… | Commande |
|---|---|
| Voir ce que fait le bot | `docker compose logs -f` |
| Arrêter le bot | `docker compose down` |
| Redémarrer le bot | `docker compose up -d` |
| Mettre à jour Freqtrade | `docker compose pull` puis `docker compose up -d` |

**Sur un serveur loué**, l'interface web n'est accessible que depuis le serveur
lui-même, pour des raisons de sécurité. Pour l'ouvrir depuis ton ordinateur :

```bash
ssh -L 8080:localhost:8080 utilisateur@adresse-du-serveur
```

Puis ouvre http://localhost:8080 sur ton ordinateur.
