# Generated by Django 4.1.3 on 2023-01-05 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_referido_lazo'),
        ('drivers', '0002_alter_driver_options_driver_timestamp_terminos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminos',
            name='conductor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
    ]