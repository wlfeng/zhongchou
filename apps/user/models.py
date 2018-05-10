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
