"""Seed du portail vitrine DimaAtlas : arbre de pages + contenu de démo.

Idempotent : relançable sans dupliquer (slugs uniques).

    python manage.py seed_portal
"""
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from wagtail.models import Page, Site


def erp(path):
    """Préfixe un chemin de démo par l'URL de l'ERP (vitrine isolée).

    Sans ERP_BASE_URL, conserve le chemin relatif (dev sur même host)."""
    base = getattr(settings, "ERP_BASE_URL", "") or ""
    return f"{base.rstrip('/')}{path}" if base else path

from portal.models import (
    HomePage, FlexPage, SolutionsIndexPage, SolutionPage,
    BlogIndexPage, ContactPage, ContactFormField,
    BrandSettings, MenuItem,
)


SOLUTIONS = [
    ("Commande à table & QR Menu", "Restauration", "menu-qr",
     "Carte digitale par QR code, commande à table, écran cuisine (KDS) temps réel et addition sans contact.",
     "/qr/"),
    ("Conciergerie & folio hôtel", "Hôtellerie", "hotel",
     "Suivi de séjour, folio client en PWA, tableau concierge en temps réel et contrôle d'accès chambre.",
     "/folio/"),
    ("Vitrine & gestion immobilière", "Immobilier", "immo",
     "Catalogue de biens, jalons de transaction et espace client — une SPA Vue 3 connectée à votre back-office.",
     "/immo/"),
    ("Parc véhicules & location", "Mobilité / Autocar", "autocar",
     "Gestion de flotte, réservations et disponibilités pour agences de location et transport.",
     "/autocar/"),
    ("Salon & prise de RDV", "Coiffure / Beauté", "coiffure",
     "Agenda intelligent, calendrier FullCalendar, rappels et fiche client pour salons et instituts.",
     "/coiffure/"),
    ("Facturation & devis", "Gestion / Finance", "facturation",
     "Devis convertis en factures, relances automatiques, export Excel/PDF et tableau de bord encaissements.",
     "/billing/"),
]

FEATURES = [
    ("🧭", "Audit métier d'abord", "On part de votre workflow réel, pas d'un template. Chaque écran sert une tâche concrète."),
    ("⚙️", "Stack maîtrisée", "Django · DRF · Vue.js · Docker. Le même socle robuste pour tous nos verticaux."),
    ("📱", "Responsive & PWA", "Pensé mobile : vos clients commandent, réservent et paient depuis leur téléphone."),
    ("🔒", "Souverain & sécurisé", "Hébergement maîtrisé, données chez vous, conformité et sauvegardes par défaut."),
    ("🚀", "Mise en prod rapide", "Provisioning containerisé : de la maquette à la prod en jours, pas en mois."),
    ("🇲🇦", "Ancré au Maroc", "Bilingue FR/AR, paiements et usages locaux, support à Casablanca et Marrakech."),
]

WORKFLOW = [
    ("Audit & cadrage", "On cartographie votre métier, vos points de friction et vos objectifs chiffrés."),
    ("Design & maquette", "Direction visuelle et prototype interactif validés avant la moindre ligne de code."),
    ("Développement", "Itérations courtes sur socle Django + Vue, démos régulières, vous suivez l'avancement."),
    ("Déploiement & suivi", "Mise en production Docker, formation de vos équipes et accompagnement continu."),
]


class Command(BaseCommand):
    help = "Crée l'arbre de pages et le contenu de démo du portail DimaAtlas."

    @transaction.atomic
    def handle(self, *args, **opts):
        root = Page.objects.get(depth=1)

        # 1. HomePage — remplace la home Wagtail par défaut.
        home = HomePage.objects.first()
        if not home:
            # supprime la page d'accueil Wagtail par défaut ("Welcome") AVANT
            # de créer la nôtre, pour libérer le slug et la racine du site.
            for default in Page.objects.filter(depth=2).exclude(
                    content_type__model='homepage'):
                default.delete()
            root = Page.objects.get(depth=1)  # recharge numchild après suppression
            home = HomePage(
                title="DimaAtlas Solutions AI Tech",
                slug="accueil",
                body=self._home_body(),
            )
            root.add_child(instance=home)
            home.save_revision().publish()
        else:
            home.body = self._home_body()
            home.save_revision().publish()

        # 2. Repointe le Site sur la home du portail.
        site = Site.objects.first()
        if not site:
            site = Site(hostname='localhost', port=80, is_default_site=True)
        site.root_page = home
        site.site_name = "DimaAtlas Solutions AI Tech"
        site.is_default_site = True
        site.save()

        # 3. Solutions
        sol_index = self._child(home, SolutionsIndexPage, "solutions",
                                title="Solutions", intro="<p>Des produits éprouvés, un métier à la fois.</p>")
        for i, (title, sector, slug, summary, demo) in enumerate(SOLUTIONS):
            self._child(sol_index, SolutionPage, slug, title=title,
                        sector=sector, summary=summary, order=i, demo_url=erp(demo),
                        body=self._solution_body(title, summary))

        # 4. Workflow (page flexible)
        self._child(home, FlexPage, "workflow", title="Workflow",
                    body=self._workflow_body())

        # 5. À propos
        self._child(home, FlexPage, "agence", title="L'agence",
                    body=self._about_body())

        # 6. Blog
        self._child(home, BlogIndexPage, "blog", title="Veille",
                    intro="<p>Nos analyses sur la digitalisation des métiers au Maroc.</p>")

        # 7. Contact (formulaire)
        self._contact(home)

        # 8. Réglages marque + menu
        self._brand()
        self._menu()

        self.stdout.write(self.style.SUCCESS("✅ Portail DimaAtlas seedé. Visitez / et /cms/"))

    # ── helpers de contenu ────────────────────────────────────────────────
    def _home_body(self):
        return [
            ("hero", {
                "eyebrow": "Agence de digitalisation des métiers",
                "heading": "Toujours au sommet du digital",
                "subheading": "DimaAtlas conçoit et déploie des solutions web sur-mesure pour digitaliser votre métier — du QR menu restaurant au folio hôtel, de l'immobilier à la facturation.",
                "tagline_ar": "دايما في القمة",
                "ctas": [
                    {"label": "Voir nos solutions", "url": "/solutions/", "style": "primary"},
                    {"label": "Parler de votre projet", "url": "/contact/", "style": "ghost"},
                ],
                "stats": [
                    {"value": "6", "unit": "", "label": "Verticaux métier"},
                    {"value": "98", "unit": "%", "label": "Mobile-first"},
                    {"value": "4167", "unit": "m", "label": "Toubkal — au sommet"},
                ],
            }),
            ("feature_grid", {
                "heading": "Une agence produit, pas un studio de templates",
                "intro": "Nous transformons un workflow métier en application web utilisable, robuste et belle.",
                "features": [{"icon": i, "title": t, "text": x} for i, t, x in FEATURES],
            }),
            ("solutions", {
                "heading": "Nos solutions verticales",
                "intro": "Chaque secteur a son app dédiée, sur un socle technique commun.",
                "solutions": [
                    {"title": t, "sector": s, "text": summ, "url": erp(demo)}
                    for (t, s, slug, summ, demo) in SOLUTIONS
                ],
            }),
            ("workflow", {
                "heading": "De l'idée au sommet",
                "intro": "Un parcours en quatre étapes, transparent et itératif.",
                "steps": [{"title": t, "text": x} for t, x in WORKFLOW],
            }),
            ("testimonial", {
                "quote": "DimaAtlas a digitalisé notre service en salle en trois semaines. Les commandes au QR ont changé notre quotidien.",
                "author": "Restaurateur",
                "role": "Marrakech",
            }),
            ("cta_section", {
                "heading": "Prêt à digitaliser votre métier ?",
                "text": "Discutons de votre cas d'usage. Première démo offerte, sans engagement.",
                "ctas": [{"label": "Démarrer le projet", "url": "/contact/", "style": "primary"}],
            }),
        ]

    def _solution_body(self, title, summary):
        return [
            ("feature_grid", {
                "heading": f"Ce que {title} apporte",
                "intro": summary,
                "features": [
                    {"icon": "✅", "title": "Pensé pour le terrain", "text": "Des écrans qui collent à votre quotidien métier."},
                    {"icon": "⚡", "title": "Temps réel", "text": "Mises à jour live (SSE) là où ça compte."},
                    {"icon": "📊", "title": "Pilotage", "text": "Tableaux de bord et exports pour décider."},
                ],
            }),
        ]

    def _workflow_body(self):
        return [
            ("hero", {
                "eyebrow": "Notre méthode",
                "heading": "Comment nous travaillons",
                "subheading": "Un process transparent, des démos régulières, zéro effet tunnel.",
                "ctas": [{"label": "Parler de votre projet", "url": "/contact/", "style": "primary"}],
            }),
            ("workflow", {
                "heading": "Quatre étapes vers le sommet",
                "intro": "L'ordre compte : on ne code rien avant d'avoir validé le besoin et la maquette.",
                "steps": [{"title": t, "text": x} for t, x in WORKFLOW],
            }),
        ]

    def _about_body(self):
        return [
            ("hero", {
                "eyebrow": "L'agence",
                "heading": "DimaAtlas Solutions AI Tech",
                "subheading": "Agence marocaine de développement de solutions web métier. Django · DRF · Vue.js · Docker.",
                "tagline_ar": "دايما في القمة",
            }),
            ("richtext", {
                "heading": "Notre conviction",
                "body": "<p>La digitalisation réussie ne vient pas d'un outil générique, mais d'une application taillée pour <strong>votre</strong> métier. Basés à Casablanca et Marrakech, nous concevons des produits web verticaux — restauration, hôtellerie, immobilier, mobilité, beauté, gestion — sur un socle technique unique et éprouvé.</p>",
            }),
            ("cta_section", {
                "heading": "Travaillons ensemble",
                "text": "Une idée, un métier à digitaliser ? Écrivez-nous.",
                "ctas": [{"label": "Nous contacter", "url": "/contact/", "style": "primary"}],
            }),
        ]

    def _contact(self, home):
        if ContactPage.objects.exists():
            return
        contact = ContactPage(
            title="Contact", slug="contact",
            intro="<p>Parlez-nous de votre projet. Réponse sous 24h ouvrées.</p>",
            thank_you_text="<p>Votre message est bien arrivé. Nous revenons vers vous très vite.</p>",
            from_address="contact@dimatlas.com",
            to_address="contact@dimatlas.com",
            subject="Nouveau message — portail DimaAtlas",
        )
        home.add_child(instance=contact)
        contact.save_revision().publish()
        fields = [
            ("Nom complet", "singleline", True),
            ("E-mail", "email", True),
            ("Téléphone", "singleline", False),
            ("Votre métier / secteur", "singleline", False),
            ("Votre projet", "multiline", True),
        ]
        for i, (label, ftype, req) in enumerate(fields):
            ContactFormField.objects.create(
                page=contact, sort_order=i, label=label,
                field_type=ftype, required=req,
            )

    def _brand(self):
        b = BrandSettings.objects.first() or BrandSettings()
        b.brand_name = "DimaAtlas Solutions AI Tech"
        b.tagline = "Toujours au sommet du digital"
        b.tagline_ar = "دايما في القمة"
        b.email = "contact@dimatlas.com"
        b.address = "Casablanca · Marrakech"
        b.footer_text = "Agence marocaine de digitalisation des métiers. Django · Vue.js · Docker."
        b.save()

    def _menu(self):
        if MenuItem.objects.exists():
            return
        items = [
            ("Solutions", "/solutions/", 1, False),
            ("Workflow", "/workflow/", 2, False),
            ("L'agence", "/agence/", 3, False),
            ("Veille", "/blog/", 4, False),
            ("Parler de votre projet", "/contact/", 5, True),
        ]
        for label, url, order, cta in items:
            MenuItem.objects.create(label=label, url=url, order=order, cta=cta)

    # ── util arbre ────────────────────────────────────────────────────────
    def _child(self, parent, klass, slug, **kwargs):
        existing = klass.objects.filter(slug=slug).first()
        if existing:
            for k, v in kwargs.items():
                setattr(existing, k, v)
            existing.save_revision().publish()
            return existing
        obj = klass(slug=slug, **kwargs)
        parent.add_child(instance=obj)
        obj.save_revision().publish()
        return obj
