from django import template

from advertisements.models import Category

register = template.Library()

@register.inclusion_tag('base/tags/category_tags.html', name='get_category_list')
def get_category_list():
    """QuerySet category item"""
    return {

        'items': Category.objects.all()
    }
