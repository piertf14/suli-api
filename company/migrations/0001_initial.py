# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultingCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_ruc', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=100)),
                ('number_telephone', models.CharField(max_length=9)),
                ('address', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=150)),
                ('position_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MiningUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
    ]
