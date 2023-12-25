from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name='capitalize_first_letter')
def capitalize_first_letter(string):
    return string[0].upper() + string[1:] if string else ''