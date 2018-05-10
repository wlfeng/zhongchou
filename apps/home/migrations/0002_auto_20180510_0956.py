# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannermodels',
            name='banner_image',
            field=models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播大图'),
        ),
    ]
