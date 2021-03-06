# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-30 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestLive', '0004_auto_20180630_0151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='Contact_Detail',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='end_date',
            field=models.DateField(verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='start_date',
            field=models.DateField(verbose_name='Start Date'),
        ),
    ]
