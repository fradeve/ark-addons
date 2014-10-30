"""Common settings and globals."""

from os.path import abspath, basename, dirname, join, normpath
from sys import path

########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Francesco de Virgilio', 'fradeve@inventati.org'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': normpath(join(DJANGO_ROOT, 'default.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'America/Los_Angeles'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = r"$uor)tb_%ak-^0$)+&bc08k)z5*a#cejgik*8d91maur^*z-m%"
########## END SECRET CONFIGURATION


########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']
########## END SITE CONFIGURATION


########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware', #FIXME
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION


########## LOGIN CONFIGURATION
LOGIN_REDIRECT_URL = '/projects'
########## END LOGIN CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin panel and documentation:
    'suit',  # should be listed in THIRD_PARTY below, but it is required here
    'django.contrib.admin',
    # 'django.contrib.admindocs',
    'django.contrib.gis',
)

THIRD_PARTY_APPS = (
    # Database migration helpers:
    'south',
    'rest_framework',
    'leaflet',
    'vectorformats',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'appcore',
    'appstats',
    'appgeostat',
    'crispy_forms',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## START TEMPLATE CONFIGURATION
CRISPY_TEMPLATE_PACK = 'bootstrap3'
########## END TEMPLATE CONFIGURATION


########## START LEAFLET CONFIGURATION
LEAFLET_CONFIG = {
    'RESET_VIEW': False,
    'NO_GLOBALS': False,
    'ATTRIBUTION_PREFIX': 'M. Ciminale, UniBa'
}
########## END LEAFLET CONFIGURATION


########## START LAYERS STYLE CONFIGURATION
LAYERS_STYLES = {
    'base': {
        'fillColor': '#468000',
        'color': 'black',
        'weight': 0.5,
        'opacity': 1.65
    },
    'settlement-area': {
        'attributes': {
            'storedarea': ''
        },
        'style': {
            'fillColor': '#beaed4',
            'color': 'black',
            'weight': 0.5,
            'opacity': 1.65
        },
        'palette': ''
    },
    'ditch-area': {
        'attributes': {
            'storedarea': ''
        },
        'style': {
            'fillColor': '#bdc9e1',
            'color': 'black',
            'weight': 0.5,
            'opacity': 1.65
        },
        'palette': ''
    },
    'ditch-number': {
        'attributes': {
            'class_n': ''
        },
        'style': {
            'fillColor': '#74a9cf',
            'color': 'green',
            'weight': 0.5,
            'opacity': 1.65,
            'fillOpacity': 0.9,
            'dashArray': 3
        },
        'palette': ''
    },
    'compound-number': {
        'attributes': {
            'class_n': ''
        },
        'style': {
            'fillColor': '#fd8d3c',
            'color': 'green',
            'weight': 0.5,
            'opacity': 1.65,
            'fillOpacity': 0.9,
            'dashArray': 3
        },
        'palette': '',
    },
    'compound-area': {
        'attributes': {
            'storedarea': ''
        },
        'style': {
            'fillColor': '#d94701',
            'color': 'black',
            'weight': 0.5,
            'opacity': 1.65
        },
        'palette': ''
    },
    'compound-access': {
        'attributes': {
            'orientation': ''
        },
        'style': {
            'fillColor': 'green',
            'color': 'green',
            'weight': 3.5,
            'opacity': 1.65
        },
        'palette': ''
    },
    'number': {
        'attributes': {
            'class_n': ''
        },
        'style': {
            'color': 'green',
            'weight': 0.5,
            'opacity': 1.65,
            'fillOpacity': 0.9,
            'dashArray': 3
        },
        'palette': {
            '1': '#a6cee3',
            '2': '#1f78b4',
            '3': '#b2df8a',
            '4': '#33a02c',
            '5': '#fb9a99',
            '6': '#e31a1c',
            '7': '#fdbf6f',
            '8': '#ff7f00',
            '9': '#cab2d6',
            '10': '#6a3d9a',
            '11': '#ffff99',
            '12': '#b15928'
        }
    }
}
########## END LAYERS STYLE CONFIGURATION


########## START GEOSTAT SETTINGS CONFIGURATION
GEOSTAT_SETTINGS = {
    'avg_ditch_perimeter': '',
    'avg_compound_perimeter': '',
    'jenk_natural_breaks_classes': '5',
    'open_compound_treshold': 5,
    # following dict defienes matches between orientation number got from
    # views.CompoundAccessTemplateView and cardinal positions. Surely you
    # don't want to change this.
    'cardinals': {0: 'E', 1: 'NE', 2: 'N', 3: 'NW',
                  4: 'W', 5: 'SW', 6: 'S', 7: 'SE'}
}
########## END GEOSTAT SETTINGS CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME
########## END WSGI CONFIGURATION
