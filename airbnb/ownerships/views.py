from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from .models import Ownership, City
from rentdates.models import RentDate
from reservations.models import Reservation
import uuid 

# Create your views here.
def landing(request):
    cities = City.objects.all()
    ownerships = Ownership.objects.all()
    return render(request, 'ownership/landing.html', {'ownerships':ownerships, 'cities':cities})

def grid(request):
    cityId=1
    dateFrom = ''
    dateTo = ''
    guests = 1
    dateFromPrint = ''
    dateToPrint = ''

    if ('city' in request.GET):
        cityId = request.GET['city']
    if ('from' in request.GET):
        dateFrom = request.GET['from']
    if ('to' in request.GET):
        dateTo = request.GET['to']
    if ('guests' in request.GET):
        guests = request.GET['guests']

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

    if(guests == ''):
        guests = 1

    ownerships = Ownership.objects.filter(city_id=cityId, rentPeriods__minimumDate__lte= dateFrom, 
        rentPeriods__maximumDate__gte= dateTo, maximumPeopleAmount__gte=guests)

    ownerships = list(ownerships)

    for ownership in ownerships:
        ownershipRentDates = RentDate.objects.filter(ownership=ownership, 
        date__gte=dateFrom, date__lte=dateTo)

        if ownershipRentDates.exists():
           ownerships.remove(ownership)


    cities = City.objects.all()

    return render(request, 'ownership/grid.html', {'ownerships':ownerships, 'cities':cities, 
    'cityId':int(cityId),'dateFrom':dateFrom, 'dateTo':dateTo, 'guests':int(guests), 
    'dateFromPrint':dateFromPrint, 'dateToPrint':dateToPrint})

def reserve(request, ownership_id):
    ownership = get_object_or_404(Ownership, pk=ownership_id)
    commission = ownership.dailyRate * 0.08
    cityId=1
    dateFrom = ''
    dateTo = ''
    guests = 1

    if ('city' in request.GET):
        cityId = request.GET['city']
    if ('from' in request.GET):
        dateFrom = request.GET['from']
    if ('to' in request.GET):
        dateTo = request.GET['to']
    if ('guests' in request.GET):
        guests = request.GET['guests']

    return render(request, 'ownership/reserve.html', {'ownership':ownership, "commission":commission, 'cityId':int(cityId),
    'dateFrom':dateFrom, 'dateTo':dateTo, 'guests':int(guests)})

def confirmation(request):
    daysAmount = days_between(request.POST['from'], request.POST['to'])
    dateList = getDayList(request.POST['from'], daysAmount)
    ownership = get_object_or_404(Ownership, pk=request.POST['ownership'])
    errorMsg = ''

    periodExists = Ownership.objects.filter(pk=request.POST['ownership'], rentPeriods__minimumDate__lte= request.POST['from'], 
    rentPeriods__maximumDate__gte= request.POST['to']).exists()

    if periodExists:

        dateExistsBetweenDates = RentDate.objects.filter(ownership=ownership, date__in=dateList).exists()

        if not dateExistsBetweenDates:
            
            try:
                reservation = Reservation(clientName=request.POST['firstname'],clientLastName= request.POST['lastname'], 
                clientEmail= request.POST['email'], ownership=ownership)
                reservation.save()

                #2da Parte 
                for date in dateList:
                    rentDate = RentDate(ownership=ownership, date=date)
                    rentDate.reservation = reservation
                    rentDate.save()

                #3ra Parte
                reservation.totalPrice = round(reservation.ownership.dailyRate * daysAmount * 1.08 , 2)
                reservation.save()
            except Exception as e:
                errorMsg = e
        else:
            errorMsg = "Hay fechas alquiladas en el periodo seleccionado."
    else:
        errorMsg = "No existe el periodo ingresado para la propiedad."

    return render(request, 'ownership/confirmation.html', {'errorMsg': errorMsg})

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