# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-10 23:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_remove_user_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='qq',
        ),
    ]
