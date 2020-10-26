from django.db import models
from ownerships.models import Ownership
from reservations.models import Reservation
from datetime import datetime

# Create your models here.
class RentDate(models.Model):
    ownership = models.ForeignKey('ownerships.Ownership', on_delete=models.CASCADE)
    reservation = models.ForeignKey('reservations.Reservation', on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now)

    def __str__(self):
        return ''