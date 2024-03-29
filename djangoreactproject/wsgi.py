"""
WSGI config for djangoreactproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
# import sys

# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoreactproject.settings')
# sys.path.append(PROJECT_ROOT + '/..')

application = get_wsgi_application()
