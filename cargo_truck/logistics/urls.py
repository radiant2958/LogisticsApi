from django.urls import path
from logistics.views import cargo_create_views,cargo_delete_views,cargo_detail_views,cargo_list_views,cargo_update_views,vehicle_update_views



urlpatterns = [
    path('cargos/create/', cargo_create_views.CargoCreateView.as_view(), name='cargo-create'),
    path('cargos/', cargo_list_views.CargoListView.as_view(), name='cargo-list'),
    path('cargos/<int:pk>/', cargo_detail_views.CargoDetailView.as_view(), name='cargo-detail'),
    path('cargos/<int:pk>/update/', cargo_update_views.CargoUpdateView.as_view(), name='cargo-update'),
    path('cargos/<int:pk>/delete/', cargo_delete_views.CargoDeleteView.as_view(), name='cargo-delete'),
    path('vehicles/<int:pk>/update/', vehicle_update_views.VehicleUpdateView.as_view(), name='vehicle-update'),
]