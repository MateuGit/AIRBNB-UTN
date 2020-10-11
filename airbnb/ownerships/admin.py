from django.contrib import admin
from .models import Ownership, Service, City, RentPeriod

class OwnershipAdmin(admin.ModelAdmin):
    list_display=('title', 'city', 'maxPeopleAmount', 'dailyRate')
    list_filter=('city', 'maxPeopleAmount')

# Register your models here.
admin.site.register(Ownership, OwnershipAdmin)
admin.site.register(Service)
admin.site.register(City)
admin.site.register(RentPeriod)