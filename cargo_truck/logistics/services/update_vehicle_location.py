import random
from logistics.models import Vehicle, Location

def update_vehicle_location():
   
    vehicles = Vehicle.objects.all()
    locations = Location.objects.all()
    for vehicle in vehicles:
        random_location = random.choice(locations)
        vehicle.current_location = random_location
        vehicle.save()

    print("Vehicle locations updated.")
