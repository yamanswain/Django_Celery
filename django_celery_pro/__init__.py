from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app

#for importing all or in symbol *
__all__ = ('celery_app',)