from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator

# Create your models here.
class Ownership(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    services = models.ManyToManyField('Service', verbose_name="list of services")
    maxPeopleAmount = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)]
        ,verbose_name=" max people amount")
    dailyRate = models.IntegerField(default=1,validators=[MinValueValidator(1)], verbose_name="daily rate")
    city = models.ForeignKey('City', on_delete=models.SET_NULL,null=True)
    rentPeriods = models.ManyToManyField('RentPeriod', verbose_name="list of rent periods")
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class RentPeriod(models.Model):
    minDate = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now)
    maxDate = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now)

    def __str__(self):
        return self.minDate.strftime(" %d-%m-%Y") + ' / ' + self.maxDate.strftime(" %d-%m-%Y")

class City(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name