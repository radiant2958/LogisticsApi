from rest_framework import serializers

from logistics.services import calculate_distance, get_location_by_zip
from logistics.models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'