# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-08-27 01:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sala', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Insumo',
            },
        ),
        migrations.CreateModel(
            name='Reservar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_solicitud', models.DateField()),
                ('hora_inicio', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(8)])),
                ('hora_fin', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(8)])),
                ('cantidad', models.SmallIntegerField(default=2, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(2)], verbose_name=b'Cantidad de personas')),
                ('estatus', models.IntegerField(choices=[(1, b'Solicitada'), (2, b'Rechazada'), (3, b'Aceptada')], default=1)),
                ('insumos', models.ManyToManyField(default=(1, 2), to='reservaciones.Insumo')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sala.Sala')),
            ],
            options={
                'ordering': ['fecha_solicitud'],
                'verbose_name': 'Reserva de salas',
                'verbose_name_plural': 'Reservar',
            },
        ),
    ]
