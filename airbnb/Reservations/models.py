from django.db import models

# Create your models here.

class Reservation(models.Model):
    creationDate = models.DateField(auto_now=True, auto_now_add=False)
    code = Reservation.objects.latest() 
    totalPrice =  models.FloatField()
    clientName = models.TextField()
    clientLastName = models.TextField()
    clientEmail = models.EmailField(max_length = 80)
    ownership = models.ForeignKey('Ownership', on_delete=models.SET_NULL,null=True)    
    
    def __str__(self):
        return "Reservation: "+str(self.code)