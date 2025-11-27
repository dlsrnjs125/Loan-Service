"""
Database configuration for Loan Service API
"""

from dataclasses import dataclass

from decouple import config


@dataclass
class DatabaseSettings:
    """PostgreSQL database configuration"""

    name: str = config("DB_NAME", default="loan_service")
    user: str = config("DB_USER", default="postgres")
    password: str = config("DB_PASSWORD", default="postgres")
    host: str = config("DB_HOST", default="localhost")
    port: int = config("DB_PORT", default=5432, cast=int)
    sslmode: str = "disable"  # 개발 환경 기본값
    conn_max_age: int = 0  # 개발 환경 기본값

    # Test database settings
    test_name: str = "test_loan_service"

    @property
    def database_url(self) -> str:
        """Generate database URL for connection"""
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    @property
    def django_config(self) -> dict:
        """Generate Django DATABASES configuration"""
        return {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": self.name,
                "USER": self.user,
                "PASSWORD": self.password,
                "HOST": self.host,
                "PORT": self.port,
                "CONN_MAX_AGE": self.conn_max_age,
                "TEST": {
                    "NAME": self.test_name,
                },
                "OPTIONS": {
                    "sslmode": self.sslmode,
                },
            }
        }
