# Generated by Django 4.1.3 on 2023-01-05 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_explore_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explore',
            name='texto',
            field=models.CharField(max_length=30),
        ),
    ]
