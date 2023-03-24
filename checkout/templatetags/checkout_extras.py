from django.template import Library

register = Library()


@register.filter
def count(value):
    return len(value)
