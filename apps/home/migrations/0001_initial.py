# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-10 06:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0002_auto_20180509_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModels',
            fields=[
                ('projectlistmodels_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='project.ProjectListModels')),
                ('banner_image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播大图')),
            ],
            options={
                'verbose_name_plural': '轮播图',
                'verbose_name': '轮播图',
                'db_table': 'banner',
            },
            bases=('project.projectlistmodels',),
        ),
        migrations.CreateModel(
            name='TitleIconModel',
            fields=[
                ('projectlistmodels_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='project.ProjectListModels')),
                ('icon_image', models.ImageField(upload_to='icon/%Y/%m', verbose_name='icon')),
            ],
            options={
                'verbose_name_plural': '展示icon',
                'verbose_name': '展示icon',
                'db_table': 'icon',
            },
            bases=('project.projectlistmodels',),
        ),
    ]