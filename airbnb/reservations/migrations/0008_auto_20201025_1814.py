# Generated by Django 2.2 on 2020-10-25 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0007_auto_20201025_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='code',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
