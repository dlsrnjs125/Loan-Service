"""
Production settings for Loan Service DRF Backend
"""

from decouple import config

from config.settings.components import APP, SECURITY

from .base import *


# Debug mode
DEBUG = False

# Allowed hosts for production
ALLOWED_HOSTS = APP.allowed_hosts

# Security settings
SECURE_SSL_REDIRECT = SECURITY.https_required
SECURE_BROWSER_XSS_FILTER = SECURITY.browser_xss_filter
SECURE_CONTENT_TYPE_NOSNIFF = SECURITY.content_type_nosniff
SESSION_COOKIE_SECURE = SECURITY.session_cookie_secure
CSRF_COOKIE_SECURE = SECURITY.csrf_cookie_secure

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Email backend for production
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# Logging configuration for production
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
            "level": "INFO",
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
            "level": "WARNING",
            "propagate": False,
        },
    },
}
