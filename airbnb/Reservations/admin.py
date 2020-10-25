from django.contrib import admin
from reservations.models import Reservation
from rentdates.admin import RentDate_Inline


class ReservationAdmin(admin.ModelAdmin):
    list_display=('creationDate', 'clientName', 'clientLastName', 'clientEmail', 'totalPrice')
    inlines=[RentDate_Inline]

    def get_readonly_fields(self, request, obj=None):
        return ['code']

# Register your models here.
admin.site.register(Reservation, ReservationAdmin)