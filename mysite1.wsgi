import os, sys
import site
#site.addsitedir('/home/user/env16/lib/python2.6/site-packages/')
site.addsitedir('/home/pruebasdjango/django-1.6/lib/python2.6/site-packages/')


sys.path.append('/home/pruebasdjango/www/mysite1')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite1.settings'

sys.path.append('/home/pruebasdjango/www')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
