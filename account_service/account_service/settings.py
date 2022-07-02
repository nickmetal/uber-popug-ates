"""
Django settings for account_service project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "test_key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "account",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "account_service.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "account_service.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# TODO: add psql
SQLITE_DB_PATH = os.environ["SQLITE_DB_PATH"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": SQLITE_DB_PATH,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

### APP settings
OAUTH_CLIENT_ID = os.environ["OAUTH_CLIENT_ID"]
OAUTH_CLIENT_SECRET = os.environ["OAUTH_CLIENT_SECRET"]
OAUTH_URL = os.environ["OAUTH_URL"]
OAUTH_TOKEN_URL = os.environ["OAUTH_TOKEN_URL"]
OAUTH_REDIRECT_URL = os.environ["OAUTH_REDIRECT_URL"]
OAUTH_ACCONT_INFO_URL = os.environ["OAUTH_ACCONT_INFO_URL"]
OAUTHLIB_INSECURE_TRANSPORT = os.environ["OAUTHLIB_INSECURE_TRANSPORT"]
RABBITMQ_DSN = os.environ.get("RABBITMQ_DSN", "amqp://guest:guest@localhost:5672/")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simple"},
    },
    "root": {
        "handlers": ["console"],
        "level": os.getenv("LOG_LEVEL", "INFO"),
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
        "pika": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False,
        },
    },
    "formatters": {
        "simple": {
            "format": "{levelname} {asctime} {name} {funcName} {message}",
            "style": "{",
        },
    },
}
# main account for money charged from workers during task creation time
COMPANY_SLUG = "UberPopug Inc."
EVENT_SCHEMA_DIR = os.environ.get("EVENT_SCHEMA_DIR", BASE_DIR.parent / "common_lib")
TASKS_EXCHANGE_NAME = "tasks-stream"
AUTH_ACCOUNT_EXCHANGE_NAME = "accounts-stream"
AUTH_ACCOUNT_TASK_QUEUE = "accounts-stream-to-task-service"
AUTH_ACCOUNT_ACCOUNT_QUEUE = "accounts-stream-to-account-service"
BILLING_EXCHANGE_NAME = "billing-account-stream"
TASKS_TO_ACCOUNT_QUEUE = "tasks-stream-to-account-service"
MONGO_DSN = os.environ["MONGO_DSN"]
MONGO_DB_NAME = os.environ["MONGO_DB_NAME"]
MONGO_ERROR_COLLECTION = os.environ["MONGO_ERROR_COLLECTION"]
