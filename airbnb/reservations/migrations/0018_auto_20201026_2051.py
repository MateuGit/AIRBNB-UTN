# Generated by Django 2.2 on 2020-10-26 23:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0017_auto_20201026_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='code',
            field=models.CharField(default=uuid.UUID('38254e76-17e6-11eb-a28d-1c872c42c89b'), max_length=100),
        ),
    ]
