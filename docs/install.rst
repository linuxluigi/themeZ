=========================
Installation instructions
=========================

themeZ can be installed using pip::

    $ python -m pip install themez

This command will fetch the archive and its dependencies from the internet and
install them. 

If you've downloaded the tarball, unpack it, and execute::

    $ python setup.py install --user

You might prefer to install it system-wide. In this case, skip the ``--user``
option and execute as superuser by prepending the command with ``sudo``.


Add in Settings
---------------

include example pictures of each theme::

    INSTALLED_APPS = [
    ...
    'wagtail.contrib.modeladmin',  # Don't repeat if it's there already
    'wagtailmenus',
    ]


    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            '   DIRS': [
                os.path.join(PROJECT_ROOT, 'templates'),
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.request',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
                    'wagtail.contrib.settings.context_processors.settings',
                    'wagtailmenus.context_processors.wagtailmenus',
                ],
            },
        },
    ]

Troubleshoot
------------

Windows users may find that these command will only works if typed from Python's
installation directory.

Some Linux distributions (e.g. Ubuntu) install Python without installing pip.
Please install it before. If you don't have root privileges, download the
get-pip.py script at https://bootstrap.pypa.io/get-pip.py and execute it as
``python get-pip.py --user``.


Development
-----------

If you want to develop for themeZ, first clone the git repository with the
command

::

    $ git clonte 

After cloning, install the dependencies with::

    $ pip install -e .[dev]

It may also be convenient to install themeZ in your system. For doing so,
please use the command

::

    $ python setup.py develop