from __future__ import absolute_import, unicode_literals

from .development import *  # noqa F405

MEDIA_ROOT = "/tmp"

SECRET_KEY = 'top-scret!'

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
INSTALLED_APPS += ("tests", )  # noqa: F405
