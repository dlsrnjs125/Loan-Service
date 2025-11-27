"""
ASGI config for Loan Service DRF Backend.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# Django 설정 모듈을 직접 import
import django

from config.settings import production as settings


django.setup()

from django.core.asgi import get_asgi_application


application = get_asgi_application()

