# Generated by Django 2.2 on 2020-10-26 23:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0018_auto_20201026_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='code',
            field=models.CharField(default=uuid.UUID('b3e275c2-17e6-11eb-b2f1-1c872c42c89b'), max_length=100),
        ),
    ]