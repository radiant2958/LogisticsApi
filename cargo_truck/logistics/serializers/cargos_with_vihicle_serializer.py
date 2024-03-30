from rest_framework import serializers
from logistics.models import Cargo, Vehicle
from logistics.services import calculate_distance


class CargoWithVehiclesWithinRadiusSerializer(serializers.ModelSerializer):
    vehicles_within_radius = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = ('id', 'pick_up_location', 'delivery_location', 'weight', 'description', 'vehicles_within_radius')

    def get_vehicles_within_radius(self, obj):
        radius = self.context.get('radius', 0)
        vehicles_list = []
        for vehicle in Vehicle.objects.all():
            distance_to_cargo = calculate_distance.calculate_distance(
                obj.pick_up_location.latitude, obj.pick_up_location.longitude,
                vehicle.current_location.latitude, vehicle.current_location.longitude
            )
            if distance_to_cargo <= radius:
                vehicles_list.append({
                    'vehicle_id': vehicle.id,
                    'unique_number': vehicle.unique_number,
                    'distance_to_cargo': distance_to_cargo
                })
        return vehicles_list
