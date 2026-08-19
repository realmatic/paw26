[realmatic studiolab]
https://realmatic.pythonanywhere.com/
https://realmatic.pythonanywhere.com/support/

? detail page, list page, testing
# https://docs.djangoproject.com/en/6.1/intro/tutorial02/

260818
#using sqlite, not MySQL
$ python manage.py startapp archive
# vi urls.py, views.py, models.py, settings.py (add app config)
$ python manage.py makemigrations archive
$ python manage.py migrate
$ python manage.py shell
>>> Record.objects.all()
>>> import datetime
>>> from django.utils import timezone
>>> r = Record(title="TARVA Crate Stand", category='WO', production_date=timezone.make_aware(datetime.datetime(2026, 8, 1, 13, 12, 50)))
>>> r.save()
>>> r.delete()

260817
# https://help.pythonanywhere.com/pages/FollowingTheDjangoTutorial/
$ mkvirtualenv env26 --python=/usr/bin/python3.10
$ workon env26
$ deactivate

$ pip install Django
$ pip install mysqlclient python-dotenv
$ pip uninstall mysqlclient
$ django-admin startproject home

$ mv home sandbox
$ update /var/www/realmatic_pythonanywhere_com_wsgi.py

$ vi webapp/settings.py
import os
from dotenv import load_dotenv
load_dotenv(BASE_DIR / '.env')
SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = os.getenv('WEB_NAME').split(',')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'debug.log',
        },
    },
    'loggers': {
        'app': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

DATABASES = {
       'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': os.getenv('DB_NAME'),
         'USER': os.getenv('DB_USER'),
         'PASSWORD': os.getenv('DB_PASSWORD'),
         'HOST': os.getenv('DB_HOST'),
     }
}

# STATIC_URL = "static/"
# for prod
# if DEBUG is False:
STATIC_URL = os.getenv('ASSETS_URL')
MEDIA_URL = os.getenv('MEDIA_URL')

# no need for local python manage.py collectstatic, using remote

$ vi .env
$ vi .gitignore
$ vi home/urls.py index, support

python manage.py createsuperuser

# MySQL console
> drop database `realmatic$default`
$ python manage.py migrate
$ python manage.py createsuperuser
# add staff user

$ git init
$ git add .
$ git status
$ git commit -a -m 'initial commit'
$ git remote add origin git@github.com:realmatic/paw26.git
$ git push -u origin main
