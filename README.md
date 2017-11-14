# themeZ

http://themez.readthedocs.io/en/latest/

init theme with https://github.com/fabiommendes/python-boilerplate

# Install

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

# Settings

## Settings File

- COLOR_STYLE: https://bootswatch.com / Default = minty

## Enviroment vars

- GOOGLE_MAPS_KEY: `UA-XXXXX-Y`

# todo

add layouts https://www.w3schools.com/bootstrap/bootstrap_templates.asp