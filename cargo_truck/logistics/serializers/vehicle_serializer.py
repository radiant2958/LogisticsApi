from rest_framework import serializers
from logistics.services import get_location_by_zip
from logistics.models import Vehicle



class VehicleSerializer(serializers.ModelSerializer):
    current_location_zip = serializers.CharField(write_only=True, required=False, max_length=20)
    city_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Vehicle
        fields = ('id', 'unique_number', 'carrying_capacity', 'current_location_zip', 'city_name')
        read_only_fields = ('id', 'city_name')

    def get_city_name(self, obj):
        return obj.current_location.city if obj.current_location else None

    def create(self, validated_data):
        location_zip = validated_data.pop('current_location_zip', None)
        if location_zip:
            location = get_location_by_zip(location_zip)
            if not location:
                raise serializers.ValidationError({"current_location_zip": "Invalid ZIP code."})
            validated_data['current_location'] = location
        return super().create(validated_data)

    def update(self, instance, validated_data):
        location_zip = validated_data.pop('current_location_zip', None)
        if location_zip:
            location = get_location_by_zip.get_location_by_zip(location_zip)
            if not location:
                raise serializers.ValidationError({"current_location_zip": "Invalid ZIP code."})
            instance.current_location = location
        return super().update(instance, validated_data)
