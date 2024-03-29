from rest_framework import serializers
from logistics.models import Cargo, Vehicle
from geopy.distance import geodesic
from logistics.services import calculate_distance

class DetailedCargoSerializer(serializers.ModelSerializer):
    all_vehicles_with_distance = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = ('pick_up_location', 'delivery_location', 'weight', 'description', 'all_vehicles_with_distance')
   
    def get_all_vehicles_with_distance(self, obj):
        vehicles = Vehicle.objects.all()
        vehicles_list = []
        for vehicle in vehicles:
            distance = calculate_distance.calculate_distance(
                obj.pick_up_location.latitude, obj.pick_up_location.longitude,
                vehicle.current_location.latitude, vehicle.current_location.longitude
            )
            vehicles_list.append({
                'vehicle_id': vehicle.id,
                'unique_number': vehicle.unique_number,
                'distance': distance
            })
        return vehicles_list


