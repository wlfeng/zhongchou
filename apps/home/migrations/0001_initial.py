# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20180509_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModels',
            fields=[
                ('projectlistmodels_ptr', models.OneToOneField(to='apps.project.ProjectListModels', primary_key=True, serialize=False, parent_link=True, auto_created=True)),
                ('banner_image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='Logo')),
            ],
            options={
                'verbose_name_plural': '轮播图',
                'verbose_name': '轮播图',
                'db_table': 'banner',
            },
            bases=('project.projectlistmodels',),
        ),
    ]
