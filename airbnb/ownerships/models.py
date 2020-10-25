from django.db import models
from datetime import datetime, date
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.conf import settings


def todayDateValidation(value):
        today = date.today()
        if value < today:
            raise ValidationError('La fecha debe ser actual o futura.')


# Create your models here.
class Ownership(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    services = models.ManyToManyField('Service', verbose_name="list of services")
    maximumPeopleAmount = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)]
        ,verbose_name=" max people amount")
    dailyRate = models.IntegerField(default=1,validators=[MinValueValidator(1)], verbose_name="daily rate")
    city = models.ForeignKey('City', on_delete=models.SET_NULL,null=True)
    rentPeriods = models.ManyToOne('RentPeriod', on_delete=models.SET_NULL, null=True, verbose_name="list of rent periods")
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class RentPeriod(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    minimumDate = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now, validators=[todayDateValidation])
    maximumDate = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now)

    def save(self, force_insert=False, force_update=False):
        if self.maximumDate < self.minimumDate:
            raise ValidationError('La fecha maxima tiene que ser mayor que la fecha minima.')
        models.Model.save(self, force_insert, force_update)

    def __str__(self):
        return self.minimumDate.strftime(" %d-%m-%Y") + ' / ' + self.maximumDate.strftime(" %d-%m-%Y")

class City(models.Model):
    name = models.CharField(max_length=50)
   
    def __str__(self):
        return self.name