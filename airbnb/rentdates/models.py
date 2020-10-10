from django.db import models
# from ownerships.models import Ownership
from reservations.models import Reservation

# Create your models here.
class RentDate(models.Model):
    ownership = models.ForeignKey('Ownership', on_delete=models.SET_NULL)
    reservation = models.ForeignKey('Reservation', on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(auto_now=True, auto_now_add=False)