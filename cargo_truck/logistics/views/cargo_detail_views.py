from rest_framework import generics
from logistics.models import Cargo
from logistics.serializers.cargo_detail_serializer import DetailedCargoSerializer


class CargoDetailView(generics.RetrieveAPIView):
    queryset = Cargo.objects.all()
    serializer_class = DetailedCargoSerializer  
