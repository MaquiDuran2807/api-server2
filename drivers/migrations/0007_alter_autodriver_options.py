# Generated by Django 4.1.3 on 2023-01-05 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0006_remove_driver_autos_autodriver'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autodriver',
            options={'verbose_name': 'AutoDriver', 'verbose_name_plural': 'AutoDrivers'},
        ),
    ]