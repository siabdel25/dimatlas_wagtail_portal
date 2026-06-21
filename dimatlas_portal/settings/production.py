"""Settings de production — dimatlas_portal.

Valeurs sensibles lues depuis l'environnement (.env via python-decouple).
Activé par DJANGO_SETTINGS_MODULE=dimatlas_portal.settings.production.
"""
from decouple import Csv, config

from .base import *  # noqa: F401,F403

DEBUG = False

SECRET_KEY = config("SECRET_KEY")
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())
CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", cast=Csv(), default="")

# Liens vers les démos de l'ERP (apps verticales hors vitrine).
ERP_BASE_URL = config("ERP_BASE_URL", default="")

# ── Base de données — PostgreSQL ──────────────────────────────────────────
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME", default="dimatlas_portal"),
        "USER": config("DB_USER", default="postgres"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST", default="db"),
        "PORT": config("DB_PORT", default="5432"),
        "CONN_MAX_AGE": 60,
    }
}

# ── Statiques servis par WhiteNoise (compressés + hashés) ─────────────────
MIDDLEWARE.insert(
    MIDDLEWARE.index("django.middleware.security.SecurityMiddleware") + 1,
    "whitenoise.middleware.WhiteNoiseMiddleware",
)
STORAGES["staticfiles"]["BACKEND"] = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

# ── Sécurité (Nginx/Traefik termine le TLS, transmet X-Forwarded-Proto) ───
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", default=True, cast=bool)
SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS", default=31_536_000, cast=int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE", default=True, cast=bool)
CSRF_COOKIE_SECURE = config("CSRF_COOKIE_SECURE", default=True, cast=bool)
X_FRAME_OPTIONS = "DENY"

try:
    from .local import *  # noqa: F401,F403
except ImportError:
    pass
