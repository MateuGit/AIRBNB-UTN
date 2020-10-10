# Generated by Django 2.2 on 2020-10-10 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerships', '0009_rentdates'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownership',
            name='rentDates',
            field=models.ManyToManyField(to='ownerships.RentDates', verbose_name='list of rent dates'),
        ),
    ]
