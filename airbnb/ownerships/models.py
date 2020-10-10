from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator

# Create your models here.
class Ownership(models.Model):
    city = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    services = models.ManyToManyField('Service', verbose_name="list of sites")
    maxPeopleAmount = models.PositiveSmallIntegerField(default=1, 
        validators=[MinValueValidator(1)]
    )
    dailyRate = models.PositiveSmallIntegerField(default=1, 
        validators=[MinValueValidator(1)]
    )
    rentDates = models.ManyToManyField('RentDate', verbose_name="list of rent dates")
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class RentDate(models.Model):
    minDate = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now)
    maxDate = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now)

    def __str__(self):
        return self.minDate.strftime(" %d-%m-%Y") + ' / ' + self.maxDate.strftime(" %d-%m-%Y")