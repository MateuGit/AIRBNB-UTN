from django.contrib import admin
from .models import Ownership, Service, RentPeriod, City

# Register your models here.
admin.site.register(Ownership)
admin.site.register(Service)
admin.site.register(RentPeriod)
admin.site.register(City)