from geopy.distance import geodesic

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Рассчитывает расстояние между двумя точками.
    
    :param lat1: Широта первой точки
    :param lon1: Долгота первой точки
    :param lat2: Широта второй точки
    :param lon2: Долгота второй точки
    :return: Расстояние между точками в милях
    """
    location1 = (lat1, lon1)
    location2 = (lat2, lon2)
    distance = geodesic(location1, location2).miles
    return distance
