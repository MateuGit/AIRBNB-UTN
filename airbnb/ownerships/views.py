from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from .models import Ownership, City

# Create your views here.
def landing(request):
    cities = City.objects.all()
    ownerships = Ownership.objects.all()
    return render(request, 'ownership/landing.html', {'ownerships':ownerships, 'cities':cities})

def grid(request):
    cityId = request.GET.get('city')
    dateFrom = request.GET['from']
    dateTo = request.GET['to']
    guests = request.GET['guests']

    if(dateFrom == ''):
        dateFrom = datetime.now()

    if(dateTo == ''):
        dateTo = datetime.now() + timedelta(days=360)

    if(guests == ''):
        guests = 1

    ownerships = Ownership.objects.filter(city_id=cityId, rentPeriods__minimumDate__gte= dateFrom, 
    rentPeriods__maximumDate__lte= dateTo, maximumPeopleAmount__gte=guests)

    cities = City.objects.all()

    return render(request, 'ownership/grid.html', {'ownerships':ownerships, 'cities':cities, 'cityId':cityId})

def reserve(request, ownership_id):
    ownership = get_object_or_404(Ownership, pk=ownership_id)
    commission = ownership.dailyRate * 0.08
    return render(request, 'ownership/reserve.html', {'ownership':ownership, "commission":commission})
