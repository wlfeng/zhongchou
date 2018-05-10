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
            if sel == 'user':
                try:
                    user = UserModels.objects.get(username=name, password=pwd_encryption(pwd))
                    request.session['islogin'] = True
                    request.session['user_id'] = user.id
                    return JsonResponse({'msg': 'user', 'sign': 0, 'url': request.session.get('url_path', '')})
                except:
                    return JsonResponse({'msg': '用户名密码不正确', 'sign': 1})
            else:
                try:
                    user = UserModels.objects.get(username=name, password=pwd_encryption(pwd))
                    request.session['islogin'] = True
                    request.session['user'] = user
                    return JsonResponse({'msg': 'member', 'sign': 0, 'url': request.session.get('url_path', '')})
                except:
                    return JsonResponse({'msg': '用户名密码不正确', 'sign': 1})
        else:
            return JsonResponse({'msg': '信息不完整', 'sign': 1})


class RegisterView(View):
    def get(self, request):
        return render(request, 'user/reg.html')

    def post(self, request):
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        sel = request.POST.get('sel')
        email = request.POST.get('email')
        print(pwd, type(pwd))
        if name and pwd and sel and email:
            user = UserModels()
            user.username = name
            user.password = pwd
            user.email = email
            user.user_type = sel
            user.save()
            request.session['islogin'] = True
            request.session['user_id'] = user.id
            return JsonResponse({'msg': 'ok', 'sign': 0, 'url': request.session.get('url_path', '')})
        else:
            return JsonResponse({'msg': '数据不完整', 'sign': 1})
