# Generated by Django 2.2 on 2020-10-25 22:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0008_auto_20201025_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='code',
            field=models.CharField(default=uuid.UUID('14802b36-1711-11eb-810c-1c872c42c89b'), max_length=100),
        ),
    ]