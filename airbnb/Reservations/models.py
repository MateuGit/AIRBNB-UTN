from django.db import models
from ownerships.models import Ownership
from datetime import datetime


# Create your models here.

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    creationDate = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now)
    code = models.CharField(max_length = 100)
    totalPrice = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    clientName = models.CharField(max_length = 30)
    clientLastName = models.CharField(max_length = 30)
    clientEmail = models.EmailField(max_length = 80)
    ownership = models.ForeignKey('ownerships.Ownership', on_delete=models.SET_NULL,null=True)   
        
    def __str__(self):
        return str(self.id)
