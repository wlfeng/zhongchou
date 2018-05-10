from django.db import models


# Create your models here.

class ProjectListModels(models.Model):
    image = models.ImageField(upload_to="project/%Y/%m", verbose_name=u"Logo", max_length=100)
    title = models.CharField(max_length=30, verbose_name='商品名称')
    type = models.CharField(max_length=10,
                            choices=(('kj', '科技'), ('sj', '设计'), ('gy', '公益'), ('ny', '农业'), ('wh', '文化')))
    introduce = models.CharField(max_length=100, verbose_name='简介')
    state = models.CharField(max_length=10, choices=(('yzc', '已众筹结束'), ('zcz', '正在众筹中'), ('wzc', '未开始众筹')))
    start_time = models.DateField(auto_now_add=True, verbose_name='创建时间')
    end_time = models.DateField(verbose_name='结束时间')
    target_money = models.IntegerField(verbose_name='目标金额', default=0)
    now_money = models.IntegerField(verbose_name='当前金额', default=0)
    peo_num = models.IntegerField(verbose_name='支持人数', default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'project'
        verbose_name_plural = verbose_name = '众筹商品'
