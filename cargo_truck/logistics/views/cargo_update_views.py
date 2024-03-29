from rest_framework import generics
from logistics.models import Cargo
from logistics.serializers.cargo_update_serializer import CargoUpdateSerializer

class CargoUpdateView(generics.UpdateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoUpdateSerializer
