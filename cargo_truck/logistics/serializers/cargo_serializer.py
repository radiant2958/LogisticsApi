from rest_framework import serializers
from logistics.services import calculate_distance, get_location_by_zip
from logistics.models import Cargo, Vehicle



class CargoSerializer(serializers.ModelSerializer):
    pick_up_zip = serializers.CharField(write_only=True, max_length=20)
    delivery_zip = serializers.CharField(write_only=True, max_length=20)
    vehicles_within_450_miles = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = ('id', 'pick_up_zip', 'delivery_zip','pick_up_location', 'delivery_location','vehicles_within_450_miles')

    def create(self, validated_data):
        pick_up_zip = validated_data.pop('pick_up_zip')
        delivery_zip = validated_data.pop('delivery_zip')
        pick_up_location = get_location_by_zip.get_location_by_zip(pick_up_zip)
        delivery_location = get_location_by_zip.get_location_by_zip(delivery_zip)
        cargo = Cargo.objects.create(**validated_data, pick_up_location=pick_up_location, delivery_location=delivery_location)
        return cargo


    def get_vehicles_within_450_miles(self, obj):
        count = 0
        for vehicle in Vehicle.objects.all():
            distance = calculate_distance.calculate_distance(
                obj.pick_up_location.latitude, obj.pick_up_location.longitude,
                vehicle.current_location.latitude, vehicle.current_location.longitude
            )
            if distance <= 450:
                count += 1
        return count