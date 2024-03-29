from rest_framework import serializers
from logistics.services import get_location_by_zip
from logistics.models import Vehicle



class VehicleSerializer(serializers.ModelSerializer):
    current_location_zip = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Vehicle
        fields = '__all__' 

    def create(self, validated_data):
        location_zip = validated_data.pop('current_location_zip', None)
        if location_zip:
            location = get_location_by_zip(location_zip)
            validated_data['current_location'] = location
        return super().create(validated_data)

    def update(self, instance, validated_data):
        location_zip = validated_data.pop('current_location_zip', None)
        if location_zip:
            instance.current_location = get_location_by_zip(location_zip)
        return super().update(instance, validated_data)