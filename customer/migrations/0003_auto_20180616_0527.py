# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 10:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20180616_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userconsulting',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_consulting', to=settings.AUTH_USER_MODEL),
        ),
    ]
