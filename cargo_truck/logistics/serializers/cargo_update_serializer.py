from rest_framework import serializers
from logistics.models import Cargo

class CargoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['weight', 'description'] 
