# Generated by Django 2.2 on 2020-10-15 01:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ownerships', '0018_auto_20201014_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
