# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-06 21:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20160806_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='last_modified',
        ),
    ]
