# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-02 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inout', '0007_auto_20170102_0146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'Entries'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='action_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]