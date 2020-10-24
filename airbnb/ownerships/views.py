from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from .models import Ownership, City

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
