from rest_framework import generics
from logistics.models import Cargo
from logistics.serializers.cargos_create_serializer import CargoCreateSerializer

class CargoCreateView(generics.CreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoCreateSerializer
