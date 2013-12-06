# spaghetti-sh way to autoload all the database settings defined by
# every ARK project in the django.conf.DATABASES dict, to enable
# data retrieving while the app is running

from appcore.models import ArkProjectModel
import django.conf as conf

for model in ArkProjectModel.objects.all():
    arkappdbname = 'ark_' + model.projectslug.encode('utf8')
    conf.settings.DATABASES[arkappdbname] = {
        'ENGINE': 'django.db.backends.mysql',
        'AUTOCOMMIT': True,
        'ATOMIC_REQUESTS': False,
        'NAME': model.arkdbname.encode('utf8'),
        'TEST_MIRROR': None,
        'CONN_MAX_AGE': 0,
        'TEST_NAME': None,
        'TIME_ZONE': 'UTC',
        'TEST_COLLATION': None,
        'OPTIONS': {},
        'HOST': model.arkdbhost.encode('utf8'),
        'USER': model.arkdbuser.encode('utf8'),
        'TEST_CHARSET': None,
        'PASSWORD': model.arkdbpassword.encode('utf8'),
        'PORT': model.arkdbport}
