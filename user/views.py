from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .models import UserModels
from django.http import JsonResponse
from utils.hash import pwd_encryption


class LoginView(View):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        name = request.POST.get('name', '')
        pwd = request.POST.get('pwd', '')
        sel = request.POST.get('sel', '')

        if name and pwd and sel:
            print(name, pwd, sel)
            try:
                user = UserModels.objects.filter(user_type=sel).get(user_name=name, user_pwd=pwd_encryption(pwd))
                return JsonResponse({'msg': user.id})
            except:
                return JsonResponse({'msg': ''})
        else:
            return JsonResponse({'msg': ''})


class RegisterView(View):
    def get(self, request):
        return render(request, 'user/reg.html')
