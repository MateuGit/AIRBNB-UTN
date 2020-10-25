from django.db import models
from ownerships.models import Ownership
from datetime import datetime


# Create your models here.

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    creationDate = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now)
    code = models.IntegerField(blank=True, null=True) #SACAR NULL
    totalPrice =  models.FloatField(null=True)
    clientName = models.CharField(max_length = 30)
    clientLastName = models.CharField(max_length = 30)
    clientEmail = models.EmailField(max_length = 80)
    ownership = models.ForeignKey('ownerships.Ownership', on_delete=models.SET_NULL,null=True)   
        
    def __str__(self):
        return "Reservation: "+ str(self.code)
