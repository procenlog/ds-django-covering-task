from django.core import urlresolvers
from django import template
register = template.Library()


@register.simple_tag()
def admin_edit(book_id):
    return urlresolvers.reverse('admin:book_store_book_change', args=(book_id,))

