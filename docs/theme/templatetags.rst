Templatetags
============

themeZ_tags
^^^^^^^^^^^

``{% load themeZ_tags %}``

google_analytics
""""""""""""""""

Add Google Analytics when a enviroment var or settings var is set with the name ``GOOGLE_ANALYTICS_KEY``.

- **Usage:** ``{% google_analytics %}``
- **Include Template:** ``themeZ/include/google-analytics.html``

get_bootswatch_theme
""""""""""""""""""""

Get a string with a https://bootswatch.com theme. To setup set ``BOOTWATCH_THEME`` in your settings with your
theme. If ``BOOTWATCH_THEME`` is not set, it will return the default theme.

- **Usage:** ``{% get_bootswatch_theme %}``

breadcrumbs
"""""""""""

Add fully rendered Breadcrumbs.

- **Usage:** ``{% breadcrumbs %}``
- **Include Template:** ``themeZ/tags/breadcrumbs.html``

get_site_root
"""""""""""""

Get the Wagtail root site for the current Wagtail site.

Example::

    {% get_site_root as site_root %}

    <a href="{% pageurl site_root %}">Home Page</a>

get_site_name
"""""""""""""

Get the Wagtail site name witch is set in ``https://example.com/admin/sites/``

Example 1::

    {% get_site_name %}

Example 2::

    {% get_site_name as site_name %}

    {% if site_name %}
        {{ site_name }}
    {% endif %}

get_copyright_year
""""""""""""""""""

Get a string with Copyright Year. If ``COPYRIGHT_BEGIN_YEAR`` is setup in the settings, than it will return
``COPYRIGHT_BEGIN_YEAR - NOW.YEAR``. To example if the COPYRIGHT_BEGIN_YEAR is 2016 and the current year is 2018 it will
return ``2016 - 2018``.

Example usage::

    Example.com © {% get_copyright_year %}
