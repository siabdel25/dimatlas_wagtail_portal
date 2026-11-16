# TODO — Portail vitrine DimaAtlas

Voir aussi [ROADMAP.md](ROADMAP.md).

## 🔴 Priorité haute

- [ ] Configurer SMTP en production : `production.py` ne définit aucun `EMAIL_*`,
      donc le formulaire de contact n'enverra pas d'e-mails
- [ ] Ajouter les variables `EMAIL_*` et `SECURE_*` dans `.env.example`
- [ ] Mettre en place les certificats TLS dans `nginx/certs/` et leur renouvellement
- [ ] Écrire des tests minimaux (aucun test pour l'instant)

## 🟠 Nettoyage du code

- [ ] `settings/base.py` : `LANGUAGE_CODE` et `TIME_ZONE` sont définis deux fois
      (`en-us`/`UTC` puis `fr`/`Africa/Casablanca`). Ne garder que la seconde définition
- [ ] `settings/base.py` : déplacer `import os` en haut du fichier
- [ ] `ERP_BASE_URL` est lu via `os.environ` (base) **et** via `decouple` (prod) :
      unifier
- [ ] Aligner la version de Python : le Dockerfile utilise 3.12, le README annonce 3.11+

## 🟡 Nettoyage de `docs/`

- [ ] Supprimer les doublons : fichiers `(1)`, copies identiques entre
      `docs/flyer/`, `docs/landingpage/landingpages/` et `docs/marketing/`
- [ ] Renommer `docs/landingpage_QRPro_qrcode_**.html` (les `*` dans le nom posent
      problème avec le shell)
- [ ] Éviter les espaces et accents dans les noms de fichiers
- [ ] Garder une seule version finale de chaque flyer (`dimaresto-flyer` v1/v2/v3)

## 🟢 Plus tard

- [ ] Sitemap et `robots.txt` (`wagtail.contrib.sitemaps`)
- [ ] Balises Open Graph / meta dans `base.html`
- [ ] CI GitHub Actions (`manage.py check`, tests, build Docker)
