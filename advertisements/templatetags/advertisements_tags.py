from django import template

from advertisements.models import Category

register = template.Library()


@register.inclusion_tag('base/tags/menu.html', name='get_menu_item')
def get_menu_item():
    """QuerySet category menu"""
    return {
        'items': Category.objects.all()
    }



