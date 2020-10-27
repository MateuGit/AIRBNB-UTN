from ownerships.models import Ownership

def getOwnershipByCityIdAndGuestsBetweenDates(cityId,guests,dateFrom,dateTo):
    return Ownership.objects.filter(city_id=cityId, rentPeriods__minimumDate__lte= dateFrom, 
        rentPeriods__maximumDate__gte= dateTo, maximumPeopleAmount__gte=guests)
        
def existsOwnershipByIdBetweenDates(id,dateFrom,dateTo):
    return Ownership.objects.filter(pk=id, rentPeriods__minimumDate__lte= dateFrom, 
    rentPeriods__maximumDate__gte= dateTo).exists()