from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class UserModels(AbstractUser):
    user_type = models.CharField(max_length=10, choices=(('gr', '个人'), ('qy', '企业')), default='gr')

    class Meta:
        db_table = 'user'
        verbose_name_plural = verbose_name = '用户信息'

    def __str__(self):
        return self.username


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
