# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-11 02:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_projecttypemodels_sm_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectlistmodels',
            name='type',
            field=models.CharField(choices=[('kj', '科技'), ('sj', '设计'), ('gy', '公益'), ('ny', '农业'), ('wh', '文化')], max_length=10),
        ),
        migrations.DeleteModel(
            name='ProjectTypeModels',
        ),
    ]