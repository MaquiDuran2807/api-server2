# Generated by Django 4.1.3 on 2023-01-06 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_home_about_remove_home_mision_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=70)),
                ('itemtitle1', models.CharField(max_length=50)),
                ('itemdescription1', models.TextField()),
                ('itemtitle2', models.CharField(max_length=50)),
                ('itemdescription2', models.TextField()),
                ('itemtitle3', models.CharField(max_length=50)),
                ('itemdescription3', models.TextField()),
                ('itemtitle4', models.CharField(max_length=50)),
                ('itemdescription4', models.TextField()),
                ('itemtitle5', models.CharField(max_length=50)),
                ('itemdescription5', models.TextField()),
                ('itemtitle6', models.CharField(max_length=50)),
                ('itemdescription6', models.TextField()),
            ],
        ),
    ]
