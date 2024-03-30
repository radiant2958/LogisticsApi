import os
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Loads data from CSV and creates vehicles'

    def handle(self, *args, **options):
        from logistics.management.commands.utils import load_data_from_csv, create_vehicles_with_random_location
        file_path = os.path.join(settings.BASE_DIR, 'uszips.csv')
        load_data_from_csv(file_path)
        create_vehicles_with_random_location(20)
        self.stdout.write(self.style.SUCCESS('Data initialization complete.'))
