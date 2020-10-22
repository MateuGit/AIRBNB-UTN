from django.shortcuts import render, get_object_or_404
from .models import Ownership

# Create your views here.
def home(request):
    ownerships = Ownership.objects.all()
    return render(request, 'ownership/home.html', {'ownerships':ownerships})

def landing(request):
    ownerships = Ownership.objects.all()
    return render(request, 'ownership/landing.html', {'ownerships':ownerships})

def grid(request):
    ownerships = Ownership.objects.all()
    return render(request, 'ownership/grid.html', {'ownerships':ownerships})

def reserve(request, ownership_id):
    ownership = get_object_or_404(Ownership, pk=ownership_id)
    commission = ownership.dailyRate * 0.08
    return render(request, 'ownership/reserve.html', {'ownership':ownership, "commission":commission})

def detail(request, ownership_id):
    ownership = get_object_or_404(Ownership, pk=ownership_id)
    commission = ownership.dailyRate * 0.08

    return render(request, "ownership/detail.html", {'ownership':ownership, "commission":commission})