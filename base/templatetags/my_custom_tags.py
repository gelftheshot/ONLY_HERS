from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg


@register.filter
def is_supermodel(user):
    try:
        return hasattr(user, 'supermodel') and user.supermodel is not None
    except user.DoesNotExist:
        return False