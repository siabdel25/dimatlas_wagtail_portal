# Roadmap — Portail vitrine DimaAtlas

Mis à jour le 16/11/2026.

## ✅ Phase 0 — Fondations (fait)

- Projet Wagtail 7.4 / Django 5.2 autonome, sorti du monorepo
- Modèles de pages : accueil, pages flexibles, catalogue de solutions, blog, contact
- Blocs StreamField (hero, grille de fonctionnalités, workflow, vitrine de
  solutions, témoignage, CTA) et snippets (identité, menu)
- Commande `seed_portal` qui génère l'arborescence
- Stack Docker de production : PostgreSQL 16, gunicorn, WhiteNoise, Nginx TLS
- Journalisation dans un fichier avec rotation
- Supports marketing : landing pages et flyers QR Pro, hôtel/riad, restaurant

## 🚧 Phase 1 — Mise en ligne (court terme)

- Configurer l'envoi d'e-mails SMTP en production (formulaire de contact)
- Obtenir le certificat TLS (Let's Encrypt) et automatiser son renouvellement
- Déployer sur le serveur et pointer les DNS `dimatlas.com` / `www`
- Rédiger le contenu réel : textes, visuels et fiches solutions
- Sauvegarder PostgreSQL et `/media/`
- Ajouter les tests de base (rendu des pages, formulaire de contact, `seed_portal`)

## 🔜 Phase 2 — Acquisition (moyen terme)

- Intégrer les landing pages de `docs/` comme pages Wagtail (QR Pro, hôtel, resto)
- SEO : sitemap, `robots.txt`, balises Open Graph, données structurées
- Mesure d'audience respectueuse du RGPD et bandeau de consentement
- Suivi des leads : stocker et exporter les soumissions du formulaire
- Contenu du blog : cas clients et démos (Marrakech)

## 💡 Phase 3 — Évolutions (long terme)

- Site multilingue FR / EN / AR (`wagtail-localize`)
- Pages de démo interactives liées à l'ERP (`ERP_BASE_URL`)
- CI GitHub Actions : lint, tests, build de l'image Docker
- Envisager un front Vue pour les démos (cf. `.gitignore`)
