# Generated by Django 4.1.3 on 2023-01-06 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_socialmedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='subtitle',
            field=models.TextField(),
        ),
    ]