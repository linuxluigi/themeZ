from __future__ import absolute_import, unicode_literals

import os
from django import template
from django.conf import settings
from django.utils.timezone import now

from themeZ.models import Page

register = template.Library()


@register.inclusion_tag('themeZ/include/google-analytics.html', takes_context=False)
def google_analytics():
    """
    Add google analytics template if enviroment or settings has 'GOOGLE_ANALYTICS_KEY'
    :return:
        google analytics template
    """
    if "GOOGLE_ANALYTICS_KEY" in os.environ:
        GOOGLE_ANALYTICS_KEY = os.environ['GOOGLE_ANALYTICS_KEY']
    else:
        GOOGLE_ANALYTICS_KEY = settings, 'GOOGLE_ANALYTICS_KEY', False

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


@register.inclusion_tag('themeZ/tags/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=2)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    """
    Get the Wagtail root page for the current wagtail website
    :return:
    Wagtail root page
    """
    return context['request'].site.root_page


@register.assignment_tag(takes_context=True)
def get_site_name(context):
    """
    Get the Wagtail site name
    :return: String - Wagtail site name
    """
    site_name = context['request'].site.site_name
    if not site_name:
        site_name = ""
    return site_name


@register.assignment_tag(takes_context=True)
def get_copyright_year(context):
    """
    Get a string from the website beginning to the current year
    """
    current_year = now().year
    copyright_begin_year = getattr(settings, 'COPYRIGHT_BEGIN_YEAR', current_year)
    if current_year == copyright_begin_year:
        copyright_year = current_year
    else:
        copyright_year = "%d - %d" % (copyright_begin_year, current_year)
    return copyright_year
