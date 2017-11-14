from __future__ import absolute_import, unicode_literals

import os
from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('themeZ/include/google-analytics.html', takes_context=False)
def google_analytics():
    """
    Add google analytics template if enviroment has 'GOOGLE_ANALYTICS_KEY'
    :return:
        google analytics template
    """
    if "GOOGLE_ANALYTICS_KEY" in os.environ:
        GOOGLE_ANALYTICS_KEY = os.environ['GOOGLE_ANALYTICS_KEY']
    else:
        GOOGLE_ANALYTICS_KEY = False

    return {
        'GOOGLE_ANALYTICS_KEY': GOOGLE_ANALYTICS_KEY,
    }


@register.simple_tag
def get_bootswatch_theme():
    """
    get a theme name from https://bootswatch.com
    need to add in settings: BOOTWATCH_THEME = 'default'
    :return:
    Color Theme as a String witch is set in settings
    """
    return getattr(settings, 'BOOTWATCH_THEME', "minty")
