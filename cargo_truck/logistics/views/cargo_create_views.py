from rest_framework import generics
from logistics.models import Cargo
from logistics.serializers.cargo_serializer import CargoSerializer

class CargoCreateView(generics.CreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
