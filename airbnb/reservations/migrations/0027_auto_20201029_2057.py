# Generated by Django 2.2 on 2020-10-29 23:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0026_auto_20201029_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='code',
            field=models.CharField(default=uuid.UUID('738e9f7f-1a42-11eb-8c03-b42e994d7310'), max_length=100),
        ),
    ]
