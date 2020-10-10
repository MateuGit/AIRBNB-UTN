from django.db import models

# Create your models here.

class Reservation(models.Model):
    creationDate = models.DateField(auto_now=True, auto_now_add=False)
    code = Reservation.objects.latest(); 
    #datos de la reserva nombre, apellido y email
    totalPrice =  models.FloatField()