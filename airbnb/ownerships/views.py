from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from .models import Ownership, City
from rentdates.models import RentDate
from reservations.models import Reservation
from .processes import *
from daos.rentDateDao import * 
from daos.ownershipDao import *
from daos.reservationDao import *
from daos.cityDao import *

# Create your views here.
def landing(request):
    cities = getAllCities()
    ownerships = getAllOwnerships()
    return render(request, 'ownership/landing.html', {'ownerships':ownerships, 'cities':cities})

def grid(request):
    cityId = setParameterValue(request,'city')
    dateFrom = setParameterValue(request,'from')
    dateTo = setParameterValue(request,'to')
    guests = setParameterValue(request,'guests')
    guests = setIfEmpty(guests,1)
    dateFromPrint = ''
    dateToPrint = ''
    
    if(dateFrom == ''):
        dateFrom = datetime.now()
    else:
        dateFrom = str(dateFrom).split(' ')[0]
        dateFromPrint = dateFrom

    if(dateTo == ''):
        dateTo = datetime.now() + timedelta(days=1)
    else:
        dateTo = str(dateTo).split(' ')[0]
        dateToPrint = dateTo

    if cityId == '':
        cityId = 1

    ownerships = getOwnershipByCityIdAndGuestsBetweenDates(cityId,guests,dateFrom,dateTo)

    ownerships = validateOwnershipsBetweenPeriods(dateFrom, dateTo,ownerships)

    cities = getAllCities()

    return render(request, 'ownership/grid.html', {'ownerships':ownerships, 'cities':cities, 
    'cityId':int(cityId),'dateFrom':dateFrom, 'dateTo':dateTo, 'guests':int(guests), 
    'dateFromPrint':dateFromPrint, 'dateToPrint':dateToPrint})

def reserve(request, ownership_id):
    ownership = get_object_or_404(Ownership, pk=ownership_id)
    commission = ownership.dailyRate * 0.08
    cityId = setParameterValue(request,'city')
    dateFrom = setParameterValue(request,'from')
    dateTo = setParameterValue(request,'to')
    guests = setParameterValue(request,'guests')
    setSessionVariables(request, ownership_id, cityId, dateFrom, dateTo, guests)

    rentDatesTaken = getRentDateByOwnership(ownership)

    return render(request, 'ownership/reserve.html', {'ownership':ownership, "commission":commission, 'cityId':int(cityId),
    'dateFrom':dateFrom, 'dateTo':dateTo, 'guests':int(guests), 'rentDatesTaken':rentDatesTaken})

def confirmation(request):
    daysAmount = days_between(request.POST['from'], request.POST['to'])
    dateList = getDayList(request.POST['from'], daysAmount)
    ownership = get_object_or_404(Ownership, pk=request.POST['ownership'])
    errorMsg = ''
    reservationCode=''
    periodExists = existsOwnershipByIdBetweenDates(request.POST['ownership'],request.POST['from'],request.POST['to'])
    
    cityId = getSessionVariable(request, 'city')
    ownershipId = getSessionVariable(request, 'ownershipId')
    ownership = get_object_or_404(Ownership, pk=ownershipId)
    dateFrom = getSessionVariable(request, 'dateFrom')
    dateTo = getSessionVariable(request, 'dateTo')
    guests = getSessionVariable(request, 'guests')

    if periodExists:

        dateExistsBetweenDates = existsRentDateByOwnershipIn(ownership,dateList)

        if not dateExistsBetweenDates:
            
            try:
                #1ra Parte
                reservation = saveReservation(request,ownership)   
                reservationCode = reservation.code  
                #2da Parte 
                saveRentDates(dateList,reservation,ownership)
                #3ra Parte
                setReservationTotalPrice(reservation,daysAmount)
            except Exception as e:
                errorMsg = e
        else:
            errorMsg = "Hay fechas alquiladas en el periodo seleccionado."
    else:
        errorMsg = "No existe el periodo ingresado para la propiedad."

    return render(request, 'ownership/confirmation.html', {'errorMsg': errorMsg, 'ownership':ownership,
    'reservationCode':reservationCode, 'cityId':cityId,'dateFrom':dateFrom, 'dateTo':dateTo, 
    'guests':guests})

