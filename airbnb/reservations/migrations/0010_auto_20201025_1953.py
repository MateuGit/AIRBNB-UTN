# Generated by Django 2.2 on 2020-10-25 22:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0009_auto_20201025_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='code',
            field=models.CharField(default=uuid.UUID('efbf1d9a-1714-11eb-8779-1c872c42c89b'), max_length=100),
        ),
    ]
