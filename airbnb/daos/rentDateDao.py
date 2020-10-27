from rentdates.models import RentDate

def saveRentDates(datesList,reservation,ownership):
  for date in datesList:
    rentDate = RentDate(ownership=ownership, date=date)
    rentDate.reservation = reservation
    rentDate.save()

def getRentDatesByOwnershipBetweenDates(ownership,dateFrom,dateTo):
  return RentDate.objects.filter(ownership=ownership, 
    date__gte=dateFrom, date__lte=dateTo)

def getRentDateByOwnership(ownership):
  return RentDate.objects.filter(ownership=ownership)

def existsRentDateByOwnershipIn(ownership,dateList):
  return RentDate.objects.filter(ownership=ownership, date__in=dateList).exists()