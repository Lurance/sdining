# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-11 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_auto_20170810_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_push',
            field=models.BooleanField(default=False, verbose_name='订单是否已推送'),
        ),
    ]
