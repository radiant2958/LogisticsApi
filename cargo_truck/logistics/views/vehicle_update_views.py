from rest_framework import generics
from logistics.models import Vehicle
from logistics.serializers.vehicle_serializer import VehicleSerializer

class VehicleUpdateView(generics.UpdateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
