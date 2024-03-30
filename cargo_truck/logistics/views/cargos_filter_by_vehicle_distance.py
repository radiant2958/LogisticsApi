from rest_framework import generics
from rest_framework.response import Response
from logistics.models import Cargo
from logistics.serializers.cargos_with_vihicle_serializer import CargoWithVehiclesWithinRadiusSerializer

class CargoVehiclesWithinRadiusView(generics.ListAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoWithVehiclesWithinRadiusSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['radius'] = float(self.request.query_params.get('radius', 0))
        return context