from rest_framework import serializers
from logistics.services import get_location_by_zip
from logistics.models import Cargo

class CargoCreateSerializer(serializers.ModelSerializer):
    pick_up_zip = serializers.CharField(write_only=True, max_length=20)
    delivery_zip = serializers.CharField(write_only=True, max_length=20)
    weight = serializers.IntegerField()
    description = serializers.CharField()

    class Meta:
        model = Cargo
        fields = ('id', 'pick_up_zip', 'delivery_zip', 'weight', 'description')

    def create(self, validated_data):
        pick_up_zip = validated_data.pop('pick_up_zip')
        delivery_zip = validated_data.pop('delivery_zip')
        pick_up_location = get_location_by_zip.get_location_by_zip(pick_up_zip)
        delivery_location = get_location_by_zip.get_location_by_zip(delivery_zip)

        cargo = Cargo.objects.create(
            pick_up_location=pick_up_location,
            delivery_location=delivery_location,
            **validated_data
        )
        return cargo