# Generated by Django 4.1.3 on 2022-12-07 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serveces', '0009_alter_services_cancelc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppkm', models.FloatField(verbose_name='precio por kilometro')),
                ('ppm', models.FloatField(verbose_name='precio por minuto')),
                ('pm', models.FloatField(verbose_name='precio minimo')),
            ],
            options={
                'verbose_name': 'Price',
                'verbose_name_plural': 'Prices',
            },
        ),
    ]