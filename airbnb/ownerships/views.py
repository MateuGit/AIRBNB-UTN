from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from .models import Ownership, City
from rentdates.models import RentDate
from reservations.models import Reservation

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
    #1ra Parte
    ownership = get_object_or_404(Ownership, pk=request.POST['ownership'])
    r = Reservation(code=10, clientName=request.POST['firstname'],clientLastName= request.POST['lastname'], 
    clientEmail= request.POST['email'], ownership=ownership)
    r.save()
    return render(request, 'ownership/confirmation.html')
