from django.forms import ValidationError
from rest_framework import generics
from django.db.models import Q
from logistics.models import Cargo
from logistics.serializers.cargos_filter import CargoFilter

class CargoWeightFilterView(generics.ListAPIView):
    serializer_class = CargoFilter

    def get_queryset(self):
        """
        Возвращает отсортированный по весу список грузов от легкого к тяжелому.
        """
        queryset = Cargo.objects.all().order_by('weight')  # Добавлен order_by для сортировки
        
        min_weight = self.request.query_params.get('min_weight', None)
        max_weight = self.request.query_params.get('max_weight', None)

        if min_weight is not None:
            try:
                min_weight = float(min_weight)
                queryset = queryset.filter(weight__gte=min_weight)
            except ValueError:
                raise ValidationError({'min_weight': ['Must be a number.']})

        if max_weight is not None:
            try:
                max_weight = float(max_weight)
                queryset = queryset.filter(weight__lte=max_weight)
            except ValueError:
                raise ValidationError({'max_weight': ['Must be a number.']})

        return queryset