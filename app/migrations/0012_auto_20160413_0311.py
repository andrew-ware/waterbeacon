# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 03:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20160413_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='timestamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='type',
            field=models.CharField(blank=True, choices=[(b'conductivity', b'Conductivity'), (b'orp', b'Oxygen Reduction Potential'), (b'odo', b'Dissolved Oxygen'), (b'turbidity', b'Turbidity'), (b'temperature', b'temperature'), (b'ph', b'Ph')], max_length=255, null=True),
        ),
    ]
