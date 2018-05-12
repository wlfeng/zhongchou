from django.db import models


# Create your models here.
class CompanyModels(models.Model):
    name = models.CharField(max_length=20, verbose_name='公司')
    image = models.ImageField(upload_to="company/%Y/%m", verbose_name="Logo", max_length=100)
    aut = models.CharField(choices=(('0', '未认证'), ('1', '已认证')), default='0', max_length=10)
    introduce = models.CharField(max_length=100, verbose_name='简介')
    phone = models.CharField(max_length=21, verbose_name='电话')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'company'
        verbose_name_plural = verbose_name = '公司'


class ProjectListModels(models.Model):
    company = models.ForeignKey(CompanyModels, verbose_name='公司')
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
    con_image = models.ImageField(upload_to="con_image/%Y/%m", verbose_name=u"Logo", max_length=100)
    flow_num = models.IntegerField(default=0, max_length=255, verbose_name='关注数量')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'project'
        verbose_name_plural = verbose_name = '众筹商品'


class MoneyModels(models.Model):
    project = models.ForeignKey(ProjectListModels, verbose_name='项目')
    money = models.IntegerField(verbose_name='价格', default=0)
    people_num = models.IntegerField(default=0, verbose_name='已购买数量')
    num = models.IntegerField(default=0, verbose_name='最大购买数量')
    is_quantity = models.CharField(max_length=5, choices=(('0', '不限量'), ('1', '限量')), default='0', verbose_name='是否限量')
    number = models.IntegerField(verbose_name='可购买商品数量', default=0)

    def __str__(self):
        msg = self.project.title + str(self.money)
        return msg

    class Meta:
        db_table = 'money'
        verbose_name_plural = verbose_name = '众筹价格'
