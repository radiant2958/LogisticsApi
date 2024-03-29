from django.apps import AppConfig
from django.conf import settings
import os



class LogisticsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'logistics'
    def ready(self):
        from django.db import IntegrityError
        from logistics.models import Initialization, Location
        from logistics.management.commands.utils import load_data_from_csv, create_vehicles_with_random_location
        try:
            init, created = Initialization.objects.get_or_create(id=1)
        except IntegrityError:
          
            init = Initialization.objects.get(id=1)
        
        if not init.data_loaded:
            file_path = os.path.join(settings.BASE_DIR, 'uszips.csv')
            load_data_from_csv(file_path)
            init.data_loaded = True
            init.save()

        if not init.vehicles_created:
            create_vehicles_with_random_location(20)
            init.vehicles_created = True
            init.save()