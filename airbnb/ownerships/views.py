from django.shortcuts import render
from .models import Ownership

# Create your views here.
def home(request):
    ownerships = Ownership.objects.all()
    return render(request, 'ownership/home.html', {'ownerships':ownerships})