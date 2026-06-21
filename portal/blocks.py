"""StreamField blocks réutilisables, rendus avec la grille Bootstrap 5.

Chaque bloc encapsule une « section » de page éditable depuis l'admin Wagtail.
Le rendu vit dans templates/portal/blocks/<nom>.html.
"""
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class CTABlock(blocks.StructBlock):
    """Bouton d'appel à l'action."""
    label = blocks.CharBlock(label="Texte du bouton", max_length=60)
    url = blocks.CharBlock(label="Lien", max_length=255)
    style = blocks.ChoiceBlock(
        choices=[('primary', 'Safran (principal)'), ('ghost', 'Contour clair')],
        default='primary',
    )

    class Meta:
        icon = 'link'
        label = "Bouton CTA"


class StatBlock(blocks.StructBlock):
    """Un chiffre clé, détourné en « altitude » dans le design."""
    value = blocks.CharBlock(label="Valeur", max_length=12, help_text="ex : 12, 98%, 4167")
    unit = blocks.CharBlock(label="Unité / suffixe", max_length=12, required=False)
    label = blocks.CharBlock(label="Libellé", max_length=60)

    class Meta:
        icon = 'list-ol'
        label = "Statistique"


class FeatureBlock(blocks.StructBlock):
    icon = blocks.CharBlock(label="Icône (emoji ou nom)", max_length=40, required=False)
    title = blocks.CharBlock(max_length=80)
    text = blocks.TextBlock(label="Description", required=False)

    class Meta:
        icon = 'pick'
        label = "Atout / feature"


class HeroBlock(blocks.StructBlock):
    """Hero signature : pic topographique animé (courbes de niveau)."""
    eyebrow = blocks.CharBlock(label="Sur-titre", max_length=80, required=False)
    heading = blocks.CharBlock(label="Titre principal", max_length=140)
    subheading = blocks.TextBlock(label="Accroche", required=False)
    tagline_ar = blocks.CharBlock(
        label="Tagline arabe", max_length=80, required=False,
        help_text="ex : دايما في القمة",
    )
    ctas = blocks.ListBlock(CTABlock(), label="Boutons", required=False)
    stats = blocks.ListBlock(StatBlock(), label="Chiffres (altitude)", required=False)

    class Meta:
        icon = 'image'
        label = "Hero (pic Atlas animé)"
        template = 'portal/blocks/hero.html'


class FeatureGridBlock(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=120, required=False)
    intro = blocks.TextBlock(required=False)
    features = blocks.ListBlock(FeatureBlock())

    class Meta:
        icon = 'grip'
        label = "Grille d'atouts"
        template = 'portal/blocks/feature_grid.html'


class WorkflowStepBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=80)
    text = blocks.TextBlock(required=False)

    class Meta:
        icon = 'arrow-right'
        label = "Étape de workflow"


class WorkflowBlock(blocks.StructBlock):
    """Process en étapes — l'ordre porte du sens (vraie séquence)."""
    heading = blocks.CharBlock(max_length=120, default="Notre workflow")
    intro = blocks.TextBlock(required=False)
    steps = blocks.ListBlock(WorkflowStepBlock())

    class Meta:
        icon = 'list-ol'
        label = "Workflow (étapes numérotées)"
        template = 'portal/blocks/workflow.html'


class SolutionCardBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=80)
    sector = blocks.CharBlock(label="Secteur / métier", max_length=60, required=False)
    text = blocks.TextBlock(required=False)
    image = ImageChooserBlock(required=False)
    url = blocks.CharBlock(label="Lien (page ou démo)", max_length=255, required=False)

    class Meta:
        icon = 'doc-full'
        label = "Carte solution"


class SolutionsShowcaseBlock(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=120, default="Nos solutions verticales")
    intro = blocks.TextBlock(required=False)
    solutions = blocks.ListBlock(SolutionCardBlock())

    class Meta:
        icon = 'grip'
        label = "Vitrine de solutions"
        template = 'portal/blocks/solutions_showcase.html'


class TestimonialBlock(blocks.StructBlock):
    quote = blocks.TextBlock()
    author = blocks.CharBlock(max_length=80)
    role = blocks.CharBlock(max_length=80, required=False)

    class Meta:
        icon = 'openquote'
        label = "Témoignage"
        template = 'portal/blocks/testimonial.html'


class CTASectionBlock(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=120)
    text = blocks.TextBlock(required=False)
    ctas = blocks.ListBlock(CTABlock(), required=False)

    class Meta:
        icon = 'plus'
        label = "Bandeau CTA"
        template = 'portal/blocks/cta_section.html'


class RichTextSection(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=120, required=False)
    body = blocks.RichTextBlock()

    class Meta:
        icon = 'doc-full'
        label = "Texte riche"
        template = 'portal/blocks/richtext.html'


class SectionStreamBlock(blocks.StreamBlock):
    """Palette de sections disponibles pour composer une page."""
    hero = HeroBlock()
    feature_grid = FeatureGridBlock()
    workflow = WorkflowBlock()
    solutions = SolutionsShowcaseBlock()
    testimonial = TestimonialBlock()
    cta_section = CTASectionBlock()
    richtext = RichTextSection()

    class Meta:
        block_counts = {'hero': {'max_num': 1}}
