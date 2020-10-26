from django.contrib import admin
from rentdates.models import RentDate
from ownerships.models import Ownership

class RentDate_Inline(admin.TabularInline):
    model=RentDate
    fk_name='reservation'
    extra=0
