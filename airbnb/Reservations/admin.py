from django.contrib import admin
from reservations.models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return ['code']

# Register your models here.
admin.site.register(Reservation, ReservationAdmin)