# Generated by Django 2.2 on 2020-10-11 14:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerships', '0010_auto_20201010_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownership',
            name='dailyRate',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='daily rate'),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='maxPeopleAmount',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='people amount'),
        ),
    ]
