
import csv
import string
from django.conf import settings
from logistics.models import Location, Vehicle
import random

def load_data_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            Location.objects.update_or_create(
                zip_code=row['zip'],
                defaults={
                    'city': row['city'],
                    'state': row['state_name'],
                    'latitude': row['lat'],
                    'longitude': row['lng'],
                },
            )
def generate_unique_number():
    """Генерирует уникальный номер для машины."""
    while True:
        unique_number = f"{random.randint(1000, 9999)}{random.choice(string.ascii_uppercase)}"
        if not Vehicle.objects.filter(unique_number=unique_number).exists():
            return unique_number


def create_vehicles_with_random_location(number_of_vehicles=20):
    for _ in range(number_of_vehicles):
        random_location = Location.objects.order_by('?').first()
        Vehicle.objects.create(
            unique_number=generate_unique_number(),  
            current_location=random_location,
            carrying_capacity=random.randint(1, 1000) 
        )