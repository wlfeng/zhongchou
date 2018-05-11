from django.contrib import admin

# Register your models here.
from .models import ProjectListModels, CompanyModels, MoneyModels

admin.site.register(ProjectListModels)
admin.site.register(CompanyModels)
admin.site.register(MoneyModels)
