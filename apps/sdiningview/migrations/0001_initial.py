# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-07 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import storage.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(storage=storage.storage.ImgStorage(), upload_to='banner/%Y/%m', verbose_name='幻灯片图')),
                ('alttext', models.CharField(blank=True, help_text='当图片加载不出显示这个', max_length=20, verbose_name='img标签alt字段')),
                ('url', models.URLField(blank=True, verbose_name='跳转地址')),
            ],
            options={
                'verbose_name': '首页幻灯片',
                'verbose_name_plural': '首页幻灯片',
            },
        ),
    ]