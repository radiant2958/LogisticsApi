from rest_framework import generics
from logistics.models import Cargo, Vehicle
from logistics.serializers.cargo_serializer import CargoSerializer

class CargoListView(generics.ListAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
