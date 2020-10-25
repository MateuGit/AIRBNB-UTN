from django.contrib import admin
from .models import Ownership, Service, City, RentPeriod
from django.core.exceptions import FieldError
from datetime import datetime
from django.contrib.auth.models import User
from rentdates.models import RentDate
from rentdates.admin import RentDate_Inline


class OwnershipAdmin(admin.ModelAdmin):
    list_display=('title', 'city', 'maximumPeopleAmount', 'dailyRate')
    list_filter=('city', 'maximumPeopleAmount')
    fieldsets = ( ('Ownership Information', {'fields': ('user', 'title', 'description', 'services', 'maximumPeopleAmount', 'dailyRate', 'city', 'rentPeriods', 'image'), 'classes': ['wide']}),)
    inlines=[RentDate_Inline]

    def get_queryset(self, request):
        qs = super(OwnershipAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            if not request.user.is_superuser:
                kwargs["queryset"] = User.objects.filter(username=request.user)
                kwargs["initial"] = kwargs["queryset"][0]
        return super(OwnershipAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class RentPeriodAdmin(admin.ModelAdmin):
    list_display=('minimumDate', 'maximumDate')

    def get_queryset(self, request):
        qs = super(RentPeriodAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            if not request.user.is_superuser:
                kwargs["queryset"] = User.objects.filter(username=request.user)
                kwargs["initial"] = kwargs["queryset"][0]
        return super(RentPeriodAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


# Register your models here.
admin.site.register(Ownership, OwnershipAdmin)
admin.site.register(Service)
admin.site.register(City)
admin.site.register(RentPeriod, RentPeriodAdmin)