activate_this = "/home/pruebasdjango/django-1.6/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

from mod_python import apache
import django

def handler(req):
    req.log_error('handler')
    req.content_type = 'text/plain'
    req.send_http_header()        # isn't required for mod_python v3.0+
    req.write('Hello, World!!!\n')
    req.write(django.get_version())
    return apache.OK

