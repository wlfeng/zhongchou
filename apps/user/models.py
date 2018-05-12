from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.project.models import ProjectListModels


# Create your models here.


class UserModels(AbstractUser):
    user_type = models.CharField(max_length=10, choices=(('gr', '个人'), ('qy', '企业')), default='gr')
    is_authentication = models.CharField(choices=(('0', '未实名认证'), ('1', '已实名认证')), default=0, max_length=10)
    title_image = models.ImageField(upload_to="project/%Y/%m", verbose_name=u"Logo", max_length=100)

    class Meta:
        db_table = 'user'
        verbose_name_plural = verbose_name = '用户信息'

    def __str__(self):
        return self.username


class AuthForUserModels(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=20)
    phone = models.CharField(verbose_name='电话', max_length=11)
    id_card = models.CharField(verbose_name='身份证号码 ', max_length=100)
    email = models.EmailField(max_length=70, unique=True)
    image = models.ImageField(upload_to="project/%Y/%m", verbose_name=u"image", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'auth'
        verbose_name_plural = verbose_name = '实名认证'


class FollowModels(models.Model):
    user = models.ForeignKey(UserModels, verbose_name='用户')
    project = models.ForeignKey(ProjectListModels, verbose_name='项目')


class AuthAndUserModels(models.Model):
    auth = models.ForeignKey(AuthForUserModels, verbose_name='实名认证')
    user = models.ForeignKey(UserModels, verbose_name='用户')


class AddressModels(models.Model):
    user = models.ForeignKey(UserModels, verbose_name='用户')
    name = models.CharField(verbose_name='姓名', max_length=20)
    phone = models.CharField(verbose_name='电话', max_length=11)
    address = models.CharField(verbose_name='地址', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'address'
        verbose_name_plural = verbose_name = '用户地址'
