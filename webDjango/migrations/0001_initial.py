# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('sinopsis', models.CharField(max_length=500)),
                ('fecha_publicacion', models.DateField()),
                ('categoria', models.CharField(max_length=30)),
            ],
        ),
    ]
