# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-19 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
