# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20160413_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, default=0.0, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='long',
            field=models.DecimalField(blank=True, decimal_places=6, default=0.0, max_digits=9, null=True),
        ),
    ]
