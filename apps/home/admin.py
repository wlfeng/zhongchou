from django.contrib import admin

# Register your models here.
from .models import BannerModels, TitleIconModel

admin.site.register(BannerModels)
admin.site.register(TitleIconModel)
