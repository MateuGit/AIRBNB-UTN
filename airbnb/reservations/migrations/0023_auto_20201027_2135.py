# Generated by Django 2.2 on 2020-10-28 00:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0022_auto_20201027_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='code',
            field=models.CharField(default=uuid.UUID('8a462426-18b5-11eb-882b-1c872c42c89b'), max_length=100),
        ),
    ]
