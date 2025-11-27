"""
Settings components for Loan Service API

This module provides domain-specific configuration classes that centralize
environment variable handling and provide type safety for Django settings.
"""

from .app import AppSettings
from .database import DatabaseSettings
from .security import SecuritySettings


# Create instances of all settings
APP = AppSettings()
DATABASE = DatabaseSettings()
SECURITY = SecuritySettings()

__all__ = [
    "APP",
    "DATABASE",
    "SECURITY",
    # Classes
    "AppSettings",
    "DatabaseSettings",
    "SecuritySettings",
]

