import pytest
from rest_framework.test import APIClient
from logistics.models import Cargo, Location, Vehicle
from django.urls import reverse

@pytest.mark.django_db
def test_create_cargo():
    client = APIClient()
    data = {
        'pick_up_zip': '10001',  # предполагается, что есть локация с таким zip-кодом
        'delivery_zip': '10002',
        'weight': 500,
        'description': 'Test Cargo',
    }
    response = client.post(reverse('cargo-create'), data, format='json')
    assert response.status_code == 201
    assert Cargo.objects.count() == 1
    assert Cargo.objects.get().description == 'Test Cargo'

@pytest.mark.django_db
def test_get_cargo_list():
    client = APIClient()
    # Создание тестовых данных опущено
    response = client.get(reverse('cargo-list'))
    assert response.status_code == 200
    assert len(response.data) == Cargo.objects.count()  

@pytest.mark.django_db
def test_get_cargo_detail():
    client = APIClient()
    cargo = Cargo.objects.create(...) 
    response = client.get(reverse('cargo-detail', kwargs={'pk': cargo.pk}))
    assert response.status_code == 200
    assert response.data['id'] == cargo.pk

@pytest.mark.django_db
def test_update_vehicle():
    client = APIClient()
    vehicle = Vehicle.objects.create(...)  
    new_location = Location.objects.create(...)  
    response = client.patch(reverse('vehicle-update', kwargs={'pk': vehicle.pk}),
                            {'current_location': new_location.pk}, format='json')
    assert response.status_code == 200
    vehicle.refresh_from_db()
    assert vehicle.current_location == new_location

@pytest.mark.django_db
def test_update_cargo():
    client = APIClient()
    cargo = Cargo.objects.create(...) 
    response = client.patch(reverse('cargo-update', kwargs={'pk': cargo.pk}),
                            {'weight': 600, 'description': 'Updated description'}, format='json')
    assert response.status_code == 200
    cargo.refresh_from_db()
    assert cargo.weight == 600
    assert cargo.description == 'Updated description'

@pytest.mark.django_db
def test_delete_cargo():
    client = APIClient()
    cargo = Cargo.objects.create(...)  
    response = client.delete(reverse('cargo-delete', kwargs={'pk': cargo.pk}))
    assert response.status_code == 204
    assert Cargo.objects.count() == 0
