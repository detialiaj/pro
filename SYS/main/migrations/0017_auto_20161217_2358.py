# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20161217_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
