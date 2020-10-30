from django.contrib import admin
from reservations.models import Reservation
from rentdates.admin import RentDate_Inline


class ReservationAdmin(admin.ModelAdmin):
    list_display=('ownership', 'creationDate', 'clientName', 'clientLastName', 'clientEmail', 'totalPrice')
    inlines=[RentDate_Inline]

    def get_queryset(self, request):
        qs = super(ReservationAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(ownership__user=request.user)

    def get_readonly_fields(self, request, obj=None):
        return ['code']

# Register your models here.
admin.site.register(Reservation, ReservationAdmin)