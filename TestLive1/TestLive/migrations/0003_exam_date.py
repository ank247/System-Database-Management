# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TestLive', '0002_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
