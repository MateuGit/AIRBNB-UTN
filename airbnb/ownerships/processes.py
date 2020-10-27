from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from .models import Ownership, City
from rentdates.models import RentDate
from reservations.models import Reservation
from daos.rentDateDao import * 
from daos.ownershipDao import *


def setParameterValue(request,parameterName):
    if parameterName in request.GET:
        return request.GET[parameterName]
    return ''

def setIfEmpty(variable,value):
    if variable=='':
        return value
    return variable


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
        dayList.append(date)
    return dayList

def validateOwnershipsBetweenPeriods(dateFrom, dateTo,ownerships):
    ownerships = list(ownerships)
    print(ownerships)
    for ownership in ownerships:
        ownershipRentDates = getRentDatesByOwnershipBetweenDates(ownership,dateFrom,dateTo)
        if ownershipRentDates.exists():
           ownerships.remove(ownership)
    return ownerships