import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "content_aggregator.settings")
app = Celery("content_aggregator")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
