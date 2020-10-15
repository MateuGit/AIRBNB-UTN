# Generated by Django 2.2 on 2020-10-12 01:39

import datetime
from django.db import migrations, models
import ownerships.models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerships', '0015_auto_20201011_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ownership',
            old_name='maxPeopleAmount',
            new_name='maximumPeopleAmount',
        ),
        migrations.RenameField(
            model_name='rentperiod',
            old_name='maxDate',
            new_name='maximumDate',
        ),
        migrations.RemoveField(
            model_name='rentperiod',
            name='minDate',
        ),
        migrations.AddField(
            model_name='rentperiod',
            name='minimumDate',
            field=models.DateField(default=datetime.datetime.now, validators=[ownerships.models.todayDateValidation]),
        ),
    ]