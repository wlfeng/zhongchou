from django.contrib import admin

# Register your models here.
from .models import UserModels, AddressModels

admin.site.register(UserModels)
admin.site.register(AddressModels)
