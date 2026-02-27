from django import template
register=template.Library()
@register.filter(name='remove_char')
def remove_chars(value,aarg):
    for charecter in aarg:
        value=value.replace(charecter,'')
    return value