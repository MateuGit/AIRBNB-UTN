from ownerships.models import City

def getAllCities():
    return City.objects.all()