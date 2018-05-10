from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class UserModels(AbstractUser):
    user_name = models.CharField(max_length=20, verbose_name='用户名', unique=True)
    user_pwd = models.CharField(max_length=50, verbose_name='密码')
    user_type = models.CharField(max_length=10, choices=(('member', '会员'), ('user', '管理')), default='member')

    class Meta:
        db_table = 'user'
        verbose_name_plural = verbose_name = '用户信息'

    def __str__(self):
        return self.user_name
