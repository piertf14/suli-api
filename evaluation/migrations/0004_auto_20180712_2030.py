# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-13 01:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20180712_1902'),
        ('evaluation', '0003_auto_20180712_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chaincustody',
            name='project',
        ),
        migrations.AddField(
            model_name='chaincustody',
            name='detail_project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_chain_custody', to='project.DetailProject'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chaincustody',
            name='area',
            field=models.CharField(max_length=100),
        ),
    ]
