"""
WSGI config for dl_re_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import sys
sys.path.append(r'C:\Users\sccdl\Desktop\Personalized-recommend-master')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dl_re_web.settings')

application = get_wsgi_application()
