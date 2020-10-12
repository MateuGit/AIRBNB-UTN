from django.contrib import admin
from .models import Ownership, Service, City, RentPeriod
from django.core.exceptions import FieldError
from datetime import datetime

class OwnershipAdmin(admin.ModelAdmin):
    list_display=('title', 'city', 'maximumPeopleAmount', 'dailyRate')
    list_filter=('city', 'maximumPeopleAmount')

# Register your models here.
admin.site.register(Ownership, OwnershipAdmin)
admin.site.register(Service)
admin.site.register(City)
admin.site.register(RentPeriod)