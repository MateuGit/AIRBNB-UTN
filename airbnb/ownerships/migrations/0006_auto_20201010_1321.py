# Generated by Django 2.2 on 2020-10-10 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerships', '0005_auto_20201010_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownership',
            name='maxDate',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='ownership',
            name='maxPeopleAmount',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='ownership',
            name='minDate',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
