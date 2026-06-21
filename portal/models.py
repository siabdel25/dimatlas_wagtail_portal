"""Modèles de pages Wagtail du portail vitrine DimaAtlas."""
from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import (
    FieldPanel, MultiFieldPanel, InlinePanel,
)
from wagtail.images.blocks import ImageChooserBlock  # noqa: F401 (utile pour migrations)
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.snippets.models import register_snippet

from .blocks import SectionStreamBlock


# ─────────────────────────────────────────────────────────────────────────
# Pages composables (StreamField de sections)
# ─────────────────────────────────────────────────────────────────────────
class HomePage(Page):
    """Page d'accueil du portail — entièrement composée de sections."""
    body = StreamField(SectionStreamBlock(), blank=True, use_json_field=True)

    content_panels = Page.content_panels + [FieldPanel('body')]
    template = 'portal/home_page.html'
    max_count = 1  # une seule home

    class Meta:
        verbose_name = "Page d'accueil (portail)"


class FlexPage(Page):
    """Page générique composable (À propos, Workflow, mentions…)."""
    body = StreamField(SectionStreamBlock(), blank=True, use_json_field=True)

    content_panels = Page.content_panels + [FieldPanel('body')]
    template = 'portal/flex_page.html'

    class Meta:
        verbose_name = "Page flexible"


# ─────────────────────────────────────────────────────────────────────────
# Solutions verticales
# ─────────────────────────────────────────────────────────────────────────
class SolutionsIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel('intro')]
    subpage_types = ['portal.SolutionPage']
    template = 'portal/solutions_index_page.html'

    def get_context(self, request):
        ctx = super().get_context(request)
        ctx['solutions'] = (
            SolutionPage.objects.child_of(self).live().order_by('order')
        )
        return ctx

    class Meta:
        verbose_name = "Index des solutions"


class SolutionPage(Page):
    """Une solution verticale (resto/QR, immo, autocar, coiffure, hôtel, facturation…)."""
    sector = models.CharField("Secteur / métier", max_length=80, blank=True)
    summary = models.TextField("Résumé (carte & SEO)", blank=True)
    order = models.PositiveSmallIntegerField("Ordre d'affichage", default=0)
    hero_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+',
    )
    demo_url = models.CharField("Lien démo live", max_length=255, blank=True)
    body = StreamField(SectionStreamBlock(), blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('sector'),
            FieldPanel('summary'),
            FieldPanel('order'),
            FieldPanel('hero_image'),
            FieldPanel('demo_url'),
        ], heading="Fiche solution"),
        FieldPanel('body'),
    ]
    parent_page_types = ['portal.SolutionsIndexPage']
    template = 'portal/solution_page.html'

    class Meta:
        verbose_name = "Solution verticale"
        ordering = ['order']


# ─────────────────────────────────────────────────────────────────────────
# Blog / veille
# ─────────────────────────────────────────────────────────────────────────
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel('intro')]
    subpage_types = ['portal.BlogPage']
    template = 'portal/blog_index_page.html'

    def get_context(self, request):
        ctx = super().get_context(request)
        ctx['posts'] = (
            BlogPage.objects.child_of(self).live().order_by('-date')
        )
        return ctx

    class Meta:
        verbose_name = "Index du blog"


class BlogPage(Page):
    date = models.DateField("Date de publication")
    excerpt = models.TextField("Chapô", blank=True)
    cover = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+',
    )
    body = StreamField(SectionStreamBlock(), blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('excerpt'),
            FieldPanel('cover'),
        ], heading="Métadonnées article"),
        FieldPanel('body'),
    ]
    parent_page_types = ['portal.BlogIndexPage']
    template = 'portal/blog_page.html'

    class Meta:
        verbose_name = "Article de blog"


# ─────────────────────────────────────────────────────────────────────────
# Contact — formulaire Wagtail avec envoi e-mail
# ─────────────────────────────────────────────────────────────────────────
class ContactFormField(AbstractFormField):
    page = ParentalKey('ContactPage', on_delete=models.CASCADE, related_name='form_fields')


class ContactPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Champs du formulaire"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldPanel('to_address'),
            FieldPanel('from_address'),
            FieldPanel('subject'),
        ], heading="Envoi e-mail"),
    ]
    template = 'portal/contact_page.html'
    landing_page_template = 'portal/contact_page_landing.html'

    class Meta:
        verbose_name = "Page contact"


# ─────────────────────────────────────────────────────────────────────────
# Réglages globaux du site (marque, footer, réseaux) + menus
# ─────────────────────────────────────────────────────────────────────────
@register_setting
class BrandSettings(BaseGenericSetting):
    brand_name = models.CharField(max_length=80, default="DimaAtlas Solutions AI Tech")
    tagline = models.CharField(max_length=120, default="Toujours au sommet du digital")
    tagline_ar = models.CharField(max_length=80, default="دايما في القمة")
    email = models.EmailField(blank=True, default="contact@dimatlas.com")
    phone = models.CharField(max_length=40, blank=True)
    address = models.CharField(max_length=160, blank=True, default="Casablanca · Marrakech")
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    footer_text = models.TextField(blank=True, default="Agence de digitalisation des métiers.")

    panels = [
        MultiFieldPanel([
            FieldPanel('brand_name'),
            FieldPanel('tagline'),
            FieldPanel('tagline_ar'),
        ], heading="Marque"),
        MultiFieldPanel([
            FieldPanel('email'),
            FieldPanel('phone'),
            FieldPanel('address'),
        ], heading="Coordonnées"),
        MultiFieldPanel([
            FieldPanel('linkedin'),
            FieldPanel('instagram'),
            FieldPanel('footer_text'),
        ], heading="Réseaux & footer"),
    ]

    class Meta:
        verbose_name = "Identité & coordonnées"


@register_snippet
class MenuItem(models.Model):
    """Lien du menu principal (ordonné)."""
    label = models.CharField(max_length=40)
    url = models.CharField(max_length=255, help_text="ex : /solutions/ ou https://…")
    order = models.PositiveSmallIntegerField(default=0)
    cta = models.BooleanField("Afficher en bouton", default=False)

    panels = [FieldPanel('label'), FieldPanel('url'), FieldPanel('order'), FieldPanel('cta')]

    class Meta:
        ordering = ['order']
        verbose_name = "Lien de menu"
        verbose_name_plural = "Menu principal"

    def __str__(self):
        return self.label
