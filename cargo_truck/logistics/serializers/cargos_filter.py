from rest_framework import serializers
from logistics.models import Cargo



class CargoFilter(serializers.ModelSerializer):
   
    class Meta:
        model = Cargo
        fields = '__all__'

