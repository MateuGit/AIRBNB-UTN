# Generated by Django 2.2 on 2020-10-11 18:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerships', '0013_auto_20201011_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownership',
            name='dailyRate',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='daily rate'),
        ),
    ]
