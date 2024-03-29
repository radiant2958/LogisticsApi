from rest_framework import generics
from logistics.models import Cargo

class CargoDeleteView(generics.DestroyAPIView):
    queryset = Cargo.objects.all()
