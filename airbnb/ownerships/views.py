from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from .models import Ownership, City
from rentdates.models import RentDate
from reservations.models import Reservation
from .processes import *


# Create your views here.
def landing(request):
    cities = City.objects.all()
    ownerships = Ownership.objects.all()
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

    ownerships = Ownership.objects.filter(city_id=cityId, rentPeriods__minimumDate__lte= dateFrom, 
        rentPeriods__maximumDate__gte= dateTo, maximumPeopleAmount__gte=guests)

    ownerships = validateOwnershipsBetweenPeriods(dateFrom, dateTo,ownerships)

    cities = City.objects.all()

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

    rentDatesTaken = RentDate.objects.filter(ownership=ownership)

    return render(request, 'ownership/reserve.html', {'ownership':ownership, "commission":commission, 'cityId':int(cityId),
    'dateFrom':dateFrom, 'dateTo':dateTo, 'guests':int(guests), 'rentDatesTaken':rentDatesTaken})

def confirmation(request):
    daysAmount = days_between(request.POST['from'], request.POST['to'])
    dateList = getDayList(request.POST['from'], daysAmount)
    ownership = get_object_or_404(Ownership, pk=request.POST['ownership'])
    errorMsg = ''
    reservationCode=''
    periodExists = Ownership.objects.filter(pk=request.POST['ownership'], rentPeriods__minimumDate__lte= request.POST['from'], 
    rentPeriods__maximumDate__gte= request.POST['to']).exists()

    if periodExists:

        dateExistsBetweenDates = RentDate.objects.filter(ownership=ownership, date__in=dateList).exists()

        if not dateExistsBetweenDates:
            
            try:
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

    return render(request, 'ownership/confirmation.html', {'errorMsg': errorMsg,'reservationCode':reservationCode})

