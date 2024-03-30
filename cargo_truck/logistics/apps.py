from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.conf import settings
import os



class LogisticsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'logistics'


 