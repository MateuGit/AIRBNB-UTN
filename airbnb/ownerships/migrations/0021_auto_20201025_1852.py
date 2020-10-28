# Generated by Django 2.2 on 2020-10-25 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ownerships', '0020_rentperiod_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ownership',
            name='rentPeriods',
        ),
        migrations.AddField(
            model_name='ownership',
            name='rentPeriods',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ownerships.RentPeriod', verbose_name='list of rent periods'),
        ),
    ]