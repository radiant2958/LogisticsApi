from django.core.management.base import BaseCommand
from logistics.models import Vehicle, Location
import random

class Command(BaseCommand):
   

    def handle(self, *args, **options):
        locations = list(Location.objects.all())
        for vehicle in Vehicle.objects.all():
            vehicle.current_location = random.choice(locations)
            vehicle.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated vehicle locations'))
