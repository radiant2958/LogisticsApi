from celery import shared_task
from logistics.models import Vehicle
from logistics.services import update_vehicle_location

@shared_task
def update_all_vehicles_locations():
    for vehicle in Vehicle.objects.all():
        update_vehicle_location.update_vehicle_location(vehicle)
