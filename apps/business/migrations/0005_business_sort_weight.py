# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-22 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_business_total_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='sort_weight',
            field=models.IntegerField(default=0, verbose_name='排序权值'),
        ),
    ]
