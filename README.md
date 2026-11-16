# DimaAtlas Solutions AI Tech — Portail vitrine

Site vitrine **Wagtail / Django** de DimaAtlas Solutions AI Tech : page d'accueil,
catalogue de solutions verticales (liens vers les démos de l'ERP), blog et page de
contact. Stack autonome, libérée de la contrainte LTS du monorepo.

- **Django** 5.2 · **Wagtail** 7.4 · **Python** 3.11+
- Base de données : SQLite en développement, PostgreSQL 16 en production
- Statiques servis par WhiteNoise · TLS et `/media/` via Nginx en production

## Structure du projet

```
dimatlas_portal/
├── dimatlas_portal/
│   └── settings/
│       ├── base.py         # configuration commune (apps, logging, Wagtail…)
│       ├── dev.py          # DEBUG=True, SQLite, e-mails console
│       └── production.py   # PostgreSQL, sécurité TLS, secrets via .env
├── portal/                 # app principale : pages, blocs, snippets, seed
├── search/                 # vue de recherche Wagtail
├── nginx/                  # conf reverse-proxy + certificats TLS
├── docs/                   # supports marketing (landing pages, flyers, pitchs)
├── docker-compose.yml      # stack de production (db + web + nginx)
├── docker-compose.override.yml  # override dev, chargé automatiquement
├── Dockerfile
└── manage.py
```

Documents projet : [ROADMAP.md](ROADMAP.md) · [TODO.md](TODO.md) ·
[CLAUDE.md](CLAUDE.md) (consignes pour les assistants IA).

### Modèles de pages (`portal/models.py`)

| Modèle | Rôle |
| --- | --- |
| `HomePage` | Page d'accueil du portail |
| `FlexPage` | Page flexible à blocs |
| `SolutionsIndexPage` / `SolutionPage` | Catalogue des solutions verticales |
| `BlogIndexPage` / `BlogPage` | Blog |
| `ContactPage` | Formulaire de contact (e-mail) |

Snippets : identité & coordonnées du site, menu principal.

## Développement local

Prérequis : Python 3.11+ et un environnement virtuel (`venv_vitrine` est utilisé
dans ce dépôt).

```bash
# 1. Dépendances
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 2. Variable de settings (développement)
export DJANGO_SETTINGS_MODULE=dimatlas_portal.settings.dev

# 3. Migrations + superutilisateur + données de démo
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_portal        # crée l'arborescence du portail

# 4. Lancer le serveur
python manage.py runserver
```

- Site : http://localhost:8000/
- Admin Wagtail : http://localhost:8000/admin/
- Admin Django : http://localhost:8000/django-admin/

## Production (Docker)

La stack `docker-compose.yml` lance **PostgreSQL 16**, **Django/Wagtail + gunicorn**
et **Nginx** (terminaison TLS + service de `/media/`).

```bash
cp .env.example .env        # renseigner SECRET_KEY, DB_PASSWORD, ALLOWED_HOSTS…
docker compose -f docker-compose.yml up -d --build
docker compose -f docker-compose.yml exec web python manage.py createsuperuser
docker compose -f docker-compose.yml exec web python manage.py seed_portal
```

Déposer le certificat TLS (`fullchain.pem` + `privkey.pem`) dans `nginx/certs/`.
Les migrations et `collectstatic` sont exécutés au démarrage du conteneur `web`.

> ⚠️ Sans `-f docker-compose.yml`, Docker charge aussi `docker-compose.override.yml`
> (mode **dev** : HTTP sur `:8000`, cookies non sécurisés, nginx désactivé).

### Test local de la stack Docker

```bash
docker compose up -d --build   # override dev auto-chargé → http://localhost:8000/
```

### Variables d'environnement (`.env`)

| Variable | Description |
| --- | --- |
| `SECRET_KEY` | Clé secrète Django (obligatoire en prod) |
| `ALLOWED_HOSTS` | Domaines autorisés, séparés par des virgules |
| `CSRF_TRUSTED_ORIGINS` | Origines de confiance CSRF |
| `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` | PostgreSQL |
| `ERP_BASE_URL` | Base des liens vers les démos de l'ERP |
| `SECURE_SSL_REDIRECT`, `SECURE_HSTS_SECONDS`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE` | Réglages de sécurité (valeurs par défaut prêtes pour la prod) |

## Journalisation

La configuration `LOGGING` (`settings/base.py`) écrit dans
`logs/dimatlas_wagtail_portal.log` avec rotation automatique (10 Mo, 5 sauvegardes)
et un miroir vers la console. Le dossier `logs/` est créé au démarrage.

## Commandes utiles

```bash
python manage.py check                 # contrôle de configuration
python manage.py seed_portal           # (re)génère l'arborescence de pages
python manage.py collectstatic         # statiques (prod)
python manage.py update_index          # réindexation de la recherche Wagtail
```

## Supports marketing (`docs/`)

Pages HTML autonomes (hors Django), à ouvrir directement dans un navigateur :

- `docs/landingpage/` — landing pages (QR Code Pro, hôtel, restaurant)
- `docs/flyer/` — flyers A4/A5 (HTML + PNG/PDF)
- `docs/marketing/` — flyers, pitchs, e-mail de prospection, médias de démo

## Dépôt

`git@github.com:Siabdel25/dimatlas_wagtail_portal.git` (branche `main`).
