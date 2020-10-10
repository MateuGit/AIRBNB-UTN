from django.db import models

# Create your models here.

class Reservation(models.Model):
    creationDate = models.DateField(auto_now=True, auto_now_add=False)
    code = Reservation.objects.latest() 
    totalPrice =  models.FloatField()
    clientName = models.TextField()
    clientLastName = models.TextField()
    clientEmail = models.EmailField(max_length = 80)
