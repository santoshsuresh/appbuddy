from django import template

register = template.Library()


@register.filter
def get_attr(obj, args):
    attribute = args
    try:
        return obj.__getattribute__(attribute)
    except AttributeError:
        return obj.__dict__.get(attribute, '')
    except:
        return ''

