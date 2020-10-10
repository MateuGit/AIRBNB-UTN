from django.contrib import admin
from .models import Ownership, Service, RentDate

# Register your models here.
admin.site.register(Ownership)
admin.site.register(Service)
admin.site.register(RentDate)