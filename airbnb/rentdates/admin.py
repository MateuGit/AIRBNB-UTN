from django.contrib import admin
from rentdates.models import RentDate
from ownerships.models import Ownership

class RentDate_Inline(admin.TabularInline):
    model=RentDate
    fk_name='ownership'
    max_num=7

# Register your models here.
admin.site.register(RentDate)
