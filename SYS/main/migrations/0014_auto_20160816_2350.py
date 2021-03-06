# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-16 21:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_delete_testmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='description',
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='fill a name', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unit',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 8, 16, 21, 50, 11, 263849, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='item',
            name='qrcode',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='QR Code'),
        ),
    ]
