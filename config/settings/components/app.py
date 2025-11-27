"""
App configuration for Loan Service API
"""

from dataclasses import dataclass
from typing import List

from decouple import config


@dataclass
class AppSettings:
    """Basic application configuration"""

    # Basic settings
    debug: bool = True
    allowed_hosts_str: str = config("ALLOWED_HOSTS", default="localhost,127.0.0.1")

    # Development/Testing flags
    use_sqlite: bool = False  # 개발 환경에서만 True로 오버라이드
    use_dummy_cache: bool = False  # 개발 환경에서만 True로 오버라이드
    verbose_logs: bool = False  # 개발 환경에서만 True로 오버라이드

    @property
    def allowed_hosts(self) -> List[str]:
        """Parse allowed hosts from comma-separated string"""
        return [host.strip() for host in self.allowed_hosts_str.split(",") if host.strip()]

    @property
    def is_development(self) -> bool:
        """Check if running in development mode"""
        return self.debug or self.use_sqlite or self.use_dummy_cache

