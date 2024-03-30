from django.db import models
import uuid

# Модель локации
class Location(models.Model):
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()

# Модель груза
class Cargo(models.Model):
    pick_up_location = models.ForeignKey(Location, related_name='cargo_pick_ups', on_delete=models.CASCADE)
    delivery_location = models.ForeignKey(Location, related_name='cargo_deliveries', on_delete=models.CASCADE)
    weight = models.IntegerField()
    description = models.TextField()

# Модель машины
class Vehicle(models.Model):
    unique_number = models.CharField(max_length=6, unique=True)
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    carrying_capacity = models.IntegerField()

