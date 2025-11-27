"""
Development settings for Loan Service DRF Backend
"""

from decouple import config

# Import domain-specific settings for local overrides
from config.settings.components import APP, DATABASE

from .base import *


# Debug mode
DEBUG = True

# Allowed hosts for development
ALLOWED_HOSTS = APP.allowed_hosts

# Static files configuration
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Security settings (relaxed for development)
SECURE_SSL_REDIRECT = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False

# Database for development (SQLite for quick setup, PostgreSQL for production-like)
# 개발 환경에서는 기본적으로 SQLite 사용 (빠른 시작)
# 환경 변수로 PostgreSQL을 명시적으로 설정하지 않은 경우 SQLite 사용
import os
if not os.environ.get("DB_HOST") or APP.use_sqlite:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Development-specific apps
INSTALLED_APPS += [
    "django_extensions",
    "debug_toolbar",
]

# Development middleware
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# Debug toolbar configuration
INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

# CORS settings for development
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Cache (use dummy cache for development)
if APP.use_dummy_cache:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        }
    }

# Email backend for development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Logging configuration for development
if APP.verbose_logs:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
                "style": "{",
            },
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "verbose",
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": False,
            },
            "django.db.backends": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": False,
            },
        },
    }

