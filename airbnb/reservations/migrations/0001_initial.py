# Generated by Django 2.2 on 2020-10-10 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ownerships', '0010_auto_20201010_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creationDate', models.DateField(auto_now=True)),
                ('code', models.IntegerField()),
                ('totalPrice', models.FloatField()),
                ('clientName', models.TextField()),
                ('clientLastName', models.TextField()),
                ('clientEmail', models.EmailField(max_length=80)),
                ('ownership', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ownerships.Ownership')),
            ],
        ),
    ]
