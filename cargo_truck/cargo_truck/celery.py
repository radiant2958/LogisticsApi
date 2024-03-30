import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cargo_truck.settings')

app = Celery('cargo_truck')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
