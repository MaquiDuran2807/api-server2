# Generated by Django 4.1.3 on 2023-01-05 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0004_rename_conductor_terminos_persona'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'verbose_name': 'Driver', 'verbose_name_plural': 'Drivers'},
        ),
        migrations.AlterModelOptions(
            name='terminos',
            options={'verbose_name': 'terminos', 'verbose_name_plural': 'terminos'},
        ),
    ]
