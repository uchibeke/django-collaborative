from django.core.wsgi import get_wsgi_application
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'collaborative.settings')
appliction = get_wsgi_application()
