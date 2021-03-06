# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-12-15 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_location_zipcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='utility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geocode', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('link', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('population', models.IntegerField(blank=True, default=0)),
                ('violation_points', models.IntegerField(blank=True, default=0)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.location')),
            ],
        ),
    ]
