from django import template

from advertisements.models import Category, City


register = template.Library()


@register.inclusion_tag('base/tags/menu.html', name='get_menu_item')
def get_menu_item():
    """QuerySet category menu"""
    return {
        'items': Category.objects.all()
    }

@register.inclusion_tag('base/tags/search_block.html', name='get_search_form')
def get_search_form():
    """QuerySet для поиска"""
    return{
        'city': City.objects.all(),
        'category': Category.objects.all()
    }



