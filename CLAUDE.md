# CLAUDE.md

Consignes pour les assistants IA qui travaillent sur ce dépôt.

## Projet

Site vitrine **Wagtail 7.4 / Django 5.2** de DimaAtlas Solutions AI Tech.
Le site est autonome : il ne dépend pas du monorepo ERP et pointe vers ses démos via
`ERP_BASE_URL`. Le contenu et l'interface sont **en français**.

## Commandes

```bash
export DJANGO_SETTINGS_MODULE=dimatlas_portal.settings.dev
python manage.py check
python manage.py makemigrations portal && python manage.py migrate
python manage.py seed_portal            # (re)crée l'arborescence de pages
python manage.py runserver
```

Docker : `docker compose up` charge l'override **dev**. Pour la prod, utiliser
`docker compose -f docker-compose.yml ...`.

## Architecture

- `dimatlas_portal/settings/` : `base.py` (commun), `dev.py`, `production.py`
  (secrets lus via `python-decouple`)
- `portal/models.py` : modèles de pages, `BrandSettings` et `MenuItem`
- `portal/blocks.py` : blocs StreamField. Chaque bloc a son template dans
  `portal/templates/portal/blocks/`
- `portal/management/commands/seed_portal.py` : données initiales. À mettre à jour
  quand on ajoute un type de page
- `search/` : recherche Wagtail (backend base de données)
- `docs/` : supports marketing HTML **autonomes**, non servis par Django

## Conventions

- Commits au format Conventional Commits, rédigés en français
  (`feat:`, `fix:`, `docs(marketing):`, `chore(docker):`…)
- Toute modification de modèle doit être accompagnée de sa migration
- Ne jamais committer `.env`, `db.sqlite3`, `logs/`, `media/`
- Remote : `git@github.com:Siabdel25/dimatlas_wagtail_portal.git`, branche `main`

## Points d'attention

- Pas encore de tests. Lancer au minimum `python manage.py check` après chaque changement
- SMTP n'est pas configuré en production (voir [TODO.md](TODO.md))
- Les fichiers de `docs/` contiennent beaucoup de doublons : vérifier avant d'éditer
  lequel est la version de référence
