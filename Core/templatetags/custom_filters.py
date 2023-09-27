from django import template

register = template.Library()


@register.filter
def replaceMinus(value, arg):
    return value.replace(arg, '_')
