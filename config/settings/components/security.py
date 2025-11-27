"""
Security configuration for Loan Service API
"""

from dataclasses import dataclass
from typing import Optional

from decouple import config


@dataclass
class SecuritySettings:
    """Security and HTTPS configuration"""

    secret_key: str = config("SECRET_KEY", default="django-insecure-change-me-in-production")
    https_required: bool = False  # 개발 환경용 HTTPS 비활성화

    # SSL/HTTPS Settings
    ssl_host: Optional[str] = config("SECURE_SSL_HOST", default=None)

    # Cookie Security
    session_cookie_secure: bool = False  # 개발 환경용 쿠키 보안 비활성화
    csrf_cookie_secure: bool = False  # 개발 환경용 쿠키 보안 비활성화

    # Browser Security
    browser_xss_filter: bool = True  # 기본값, 각 환경별에서 오버라이드
    content_type_nosniff: bool = True  # 기본값, 각 환경별에서 오버라이드

    @property
    def is_production_ready(self) -> bool:
        """Check if security is configured for production"""
        return self.secret_key != "django-insecure-change-me-in-production" and self.https_required

    @property
    def django_config(self) -> dict:
        """Generate Django security configuration"""
        return {
            "SECRET_KEY": self.secret_key,
            "SECURE_SSL_HOST": self.ssl_host,
            "SESSION_COOKIE_SECURE": self.session_cookie_secure,
            "CSRF_COOKIE_SECURE": self.csrf_cookie_secure,
            "SECURE_BROWSER_XSS_FILTER": self.browser_xss_filter,
            "SECURE_CONTENT_TYPE_NOSNIFF": self.content_type_nosniff,
        }

