from django.core.exceptions import ObjectDoesNotExist
from django.forms import ValidationError
from logistics.models import Location

def get_location_by_zip(zip_code):
    """
    Поиск локации по zip-коду.
    
    :param zip_code: Zip-код для поиска или создания локации.
    :return: объект модели Location.
    """
    try:
        location = Location.objects.get(zip_code=zip_code)
    except ObjectDoesNotExist:
        raise ValidationError(f"Location with zip code {zip_code} not found.")
    return location
