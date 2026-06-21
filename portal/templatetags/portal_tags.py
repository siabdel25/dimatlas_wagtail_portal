from django import template
from portal.models import MenuItem

register = template.Library()


@register.simple_tag
def main_menu():
    return MenuItem.objects.all()
