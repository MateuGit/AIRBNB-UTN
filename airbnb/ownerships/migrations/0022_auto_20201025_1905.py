# Generated by Django 2.2 on 2020-10-25 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerships', '0021_auto_20201025_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ownership',
            name='rentPeriods',
        ),
        migrations.AddField(
            model_name='ownership',
            name='rentPeriods',
            field=models.ManyToManyField(to='ownerships.RentPeriod', verbose_name='list of rent periods'),
        ),
    ]
