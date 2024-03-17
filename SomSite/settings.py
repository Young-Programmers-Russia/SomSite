"""
Django's settings for SomSite project.

Generated by "django-admin startproject" using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import environ
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent
APPS_DIR = BASE_DIR / "SomSite" / "apps"

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    SECRET_KEY=(str, "django-insecure-zkr=v=#n447@0+rn)$h*igax2w5m7jyz39z)#0ak@no3ll#)yc"),
    ALLOWED_HOSTS=(list, ['127.0.0.1']),
    CSRF_TRUSTED_ORIGINS=(list, []),
    DATABASE_URL=(str, "sqlite:///DATABASE")
)
env.read_env(BASE_DIR / ".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",

    "SomSite.apps.main",
    "SomSite.apps.mods",
    "SomSite.apps.servers",
    "SomSite.apps.users",
    "SomSite.apps.launcher_download",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "SomSite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "misc.context_processors.context_processor.add_variable_to_context"
            ]
        },
    },
]

WSGI_APPLICATION = "SomSite.wsgi.application"

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": env.db("DATABASE_URL"),
}

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = "ru-RU"
USE_I18N = True

TIME_ZONE = "Europe/Moscow"
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [
    ("general", BASE_DIR / "static" / "general"),
    ("main", APPS_DIR / "main" / "static"),
    ("users", APPS_DIR / "users" / "static"),
    ("mods", APPS_DIR / "mods" / "static"),
    ("servers", APPS_DIR / "servers" / "static"),
    ("launcher", APPS_DIR / "launcher_download" / "static")
]

# Media files (Files from user input from forms)

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# User model and redirects

AUTH_USER_MODEL = "users.CustomUser"
LOGIN_REDIRECT_URL = "/account/profile"
LOGIN_URL = "/account/login"
LOGOUT_REDIRECT_URL = "/account/login"
