# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-11 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20180511_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneymodels',
            name='is_quantity',
            field=models.CharField(choices=[('0', '不限量'), ('1', '限量')], default='0', max_length=5, verbose_name='是否限量'),
        ),
    ]
