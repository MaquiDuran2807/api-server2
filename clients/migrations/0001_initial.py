# Generated by Django 4.1.3 on 2023-01-04 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, db_index=True, max_length=300)),
                ('tokenNotifi', models.CharField(blank=True, db_index=True, max_length=400)),
                ('identification', models.IntegerField(verbose_name='cedula')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('genero', models.CharField(choices=[('M', 'masculino'), ('F', 'femenino'), ('O', 'otro')], default='femenino', max_length=2)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('img', models.ImageField(upload_to='Client')),
                ('imgcc', models.ImageField(blank=True, upload_to='Client', verbose_name='documento de identidad')),
                ('tel', models.IntegerField(verbose_name='numero celular')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Saldo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.IntegerField()),
                ('frecarga', models.DateTimeField(verbose_name='fecha recarga')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
            options={
                'verbose_name': 'saldo_cliente',
                'verbose_name_plural': 'saldos',
            },
        ),
        migrations.CreateModel(
            name='Referido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lazo', models.CharField(choices=[('familiar', 'f'), ('amigo', 'a'), ('conocido', 'c')], default='amigo', max_length=10)),
                ('referidos', models.ManyToManyField(blank=True, related_name='referidos', to='clients.client')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
            options={
                'verbose_name': 'Referido',
                'verbose_name_plural': 'Referidos',
            },
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificaciones', models.IntegerField()),
                ('comentario', models.CharField(blank=True, max_length=150, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
            options={
                'verbose_name': 'calificacion',
                'verbose_name_plural': 'calificaciones',
            },
        ),
    ]
