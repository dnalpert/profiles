# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 20:19
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20170101_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
    ]
