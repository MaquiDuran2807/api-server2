# Generated by Django 4.1.3 on 2022-12-07 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serveces', '0005_alter_services_tpedido_alter_services_ttake_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='cancelc',
            field=models.CharField(default='none', max_length=20),
            preserve_default=False,
        ),
    ]
