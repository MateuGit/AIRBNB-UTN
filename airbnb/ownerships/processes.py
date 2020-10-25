from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from .models import Ownership, City
from rentdates.models import RentDate
from reservations.models import Reservation


def setParameterValue(request,parameterName):
    if parameterName in request.GET:
        return request.GET[parameterName]
    return ''

def saveRentDates(datesList,reservation,ownership):
  for date in datesList:
    rentDate = RentDate(ownership=ownership, date=date)
    rentDate.reservation = reservation
    rentDate.save()

def setIfEmpty(variable,value):
    if variable=='':
        return value
    return variable

def validateOwnershipsBetweenPeriods(dateFrom, dateTo,ownerships):
    ownerships = list(ownerships)
    for ownership in ownerships:
        ownershipRentDates = RentDate.objects.filter(ownership=ownership, 
        date__gte=dateFrom, date__lte=dateTo)

        if ownershipRentDates.exists():
           ownerships.remove(ownership)
    return ownerships

def saveReservation(request,ownership):
    reservation = Reservation(clientName=request.POST['firstname'],clientLastName= request.POST['lastname'], 
    clientEmail= request.POST['email'], ownership=ownership)
    reservation.save()
    return reservation

def setReservationTotalPrice(reservation,daysAmount):
    reservation.totalPrice = round(reservation.ownership.dailyRate * daysAmount * 1.08 , 2)
    reservation.save()
    
def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    days = timedelta(1)
    new_date = d1 - days
    return abs((d2 - new_date).days)

def getDayList(dateFrom, daysAmount):
    dayList = []
    d1 = datetime.strptime(dateFrom, "%Y-%m-%d")
    for i in range(daysAmount):
        date = d1 + timedelta(days=i)
        # dayList.append(str(date.year) + '-' + str(date.month) + '-' + str(date.day))
        dayList.append(date)
    return dayList