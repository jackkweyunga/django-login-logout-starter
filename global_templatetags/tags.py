from django import template
from config import settings

register = template.Library()

@register.filter
def add_class(field, class_name):
    return field.as_widget(attrs={
        "class": " ".join((field.css_classes(), class_name))
    })

@register.simple_tag
def site_name():
    return settings.SITE_NAME