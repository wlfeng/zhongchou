# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectListModels',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('image', models.ImageField(verbose_name='Logo', upload_to='project/%Y/%m')),
                ('title', models.CharField(verbose_name='商品名称', max_length=30)),
                ('type', models.CharField(choices=[('kj', '科技'), ('sj', '设计'), ('gy', '公益'), ('ny', '农业'), ('wh', '文化')], max_length=10)),
                ('introduce', models.CharField(verbose_name='简介', max_length=100)),
                ('state', models.CharField(choices=[('yzc', '已众筹结束'), ('zcz', '正在众筹中'), ('wzc', '未开始众筹')], max_length=10)),
                ('start_time', models.DateField(verbose_name='创建时间', auto_now_add=True)),
                ('end_time', models.DateField(verbose_name='结束时间', auto_now=True)),
                ('target_money', models.IntegerField(default=0, verbose_name='目标金额')),
                ('now_money', models.IntegerField(default=0, verbose_name='当前金额')),
                ('peo_num', models.IntegerField(default=0, verbose_name='支持人数')),
            ],
            options={
                'verbose_name': '众筹商品',
                'verbose_name_plural': '众筹商品',
                'db_table': 'project',
            },
        ),
    ]
