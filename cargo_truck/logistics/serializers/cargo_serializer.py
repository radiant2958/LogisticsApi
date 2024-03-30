from rest_framework import serializers
from logistics.services import calculate_distance
from logistics.models import Cargo, Vehicle



class CargoSerializer(serializers.ModelSerializer):
    vehicles_within_450_miles = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = ('id', 'pick_up_location', 'delivery_location','vehicles_within_450_miles',)

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