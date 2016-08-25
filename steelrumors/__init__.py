# -*- coding: utf-8 -*-
from settings.celery import app as celery_app # noqa:F401

__version__ = '0.0.0'
__version_info__ = tuple([int(num) if num.isdigit() else num for num in __version__.replace('-', '.', 1).split('.')])
