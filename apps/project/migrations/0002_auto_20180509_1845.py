# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectlistmodels',
            name='end_time',
            field=models.DateField(verbose_name='结束时间'),
        ),
    ]
