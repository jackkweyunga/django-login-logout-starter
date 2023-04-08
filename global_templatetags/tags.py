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


@register.filter
def add_class_remix(fieldname):
    try:
        if fieldname.field.widget.input_type == 'select':
            return fieldname.as_widget(attrs={
                "class": "chosen-select bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 "
                         "dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 "
                         "dark:focus:border-blue-500"})
        elif fieldname.field.widget.input_type == 'checkbox':
            print("Found ---")
            return fieldname.as_widget(attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 "
                         "focus:border-blue-500 block p-2.5 dark:bg-gray-700 dark:border-gray-600 "
                         "dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 "
                         "dark:focus:border-blue-500"})
        else:
            return fieldname.as_widget(attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 "
                         "focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 "
                         "dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 "
                         "dark:focus:border-blue-500"})
    except AttributeError:
        return fieldname.as_widget(attrs={
            "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 "
                     "focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 "
                     "dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 "
                     "dark:focus:border-blue-500"})


