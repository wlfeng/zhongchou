from django.db import models

from apps.project.models import ProjectListModels


class BannerModels(ProjectListModels):
    banner_image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="轮播大图", max_length=100)

    class Meta:
        db_table = 'banner'
        verbose_name_plural = verbose_name = '轮播图'

    def __str__(self):
        return self.title
