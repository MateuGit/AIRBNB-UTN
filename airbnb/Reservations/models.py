from django.db import models
from ownerships.models import Ownership


# Create your models here.

class Reservation(models.Model):
    creationDate = models.DateField(auto_now=True, auto_now_add=False)
    code = models.IntegerField(blank=True, null=True) #SACAR NULL
    totalPrice =  models.FloatField()
    clientName = models.CharField(max_length = 30)
    clientLastName = models.CharField(max_length = 30)
    clientEmail = models.EmailField(max_length = 80)
    ownership = models.ForeignKey('ownerships.Ownership', on_delete=models.SET_NULL,null=True)    
    
    def __str__(self):
        return "Reservation: "+ str(self.code)
