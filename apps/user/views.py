from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .models import UserModels, AuthAndUserModels, AuthForUserModels
from django.http import JsonResponse
from utils.hash import pwd_encryption


class LoginView(View):
    def get(self, request):
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        return render(request, 'user/login.html', {'user': user})

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
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        return render(request, 'user/reg.html', {'user': user})

    def post(self, request):
        name = request.POST.get('name')
        pwd = request.POST.get('pwd').encode('utf-8')
        sel = request.POST.get('sel')
        email = request.POST.get('email')
        print(pwd, type(pwd))
        if name and pwd and sel and email:
            user = UserModels()
            user.username = name
            user.password = pwd_encryption(pwd)
            user.email = email
            user.user_type = sel
            user.save()
            request.session['islogin'] = True
            request.session['user_id'] = user.id
            return JsonResponse({'msg': 'ok', 'sign': 0, 'url': request.session.get('url_path', '')})
        else:
            return JsonResponse({'msg': '数据不完整', 'sign': 1})


class To_PayView(View):
    def post(self, request):
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        return render(request, 'home/index.html', {'user': user})


class UserdetailView(View):
    def get(self, request):
        total = 'userdetail'
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        print(user.title_image)
        return render(request, 'user/member.html', {'user': user, 'total': total})


class MyProjectView(View):
    def get(self, request):
        total = 'myproject'
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        return render(request, 'user/minecrowdfunding.html', {'user': user, 'total': total})


class UserAuthView(View):
    def get(self, request):
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        return render(request, 'user/accttype.html', {'user': user})


class UserApplyOneView(View):
    def get(self, request):
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        return render(request, 'user/apply.html', {'user': user})

    def post(self, request):
        # {'name': name, 'pwd': pwd, 'phone': phone},
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        name = request.POST.get('name', '')
        pwd = request.POST.get('pwd', '')
        phone = request.POST.get('phone', '')
        auth = AuthForUserModels()
        auth.name = name
        auth.id_card = pwd
        auth.phone = phone
        auth.save()
        auth_user = AuthAndUserModels()
        auth_user.user = user
        auth_user.auth = auth
        auth_user.save()
        return JsonResponse({'state': '200', 'user': user})


class UserApplyTwoView(View):
    def get(self, request):
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        return render(request, 'user/apply-1.html', {'user': user})


class UserApplyThreeView(View):
    def get(self, request):
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        return render(request, 'user/apply-2.html', {'user': user})

    def post(self, request):
        email = request.POST.get('email')
        try:

            aut = AuthAndUserModels.objects.get(user_id=request.session['user_id'])
            aut.auth.email = email
            aut.auth.save()
        except Exception as e:
            print(
                e
            )

        print(email)
        return JsonResponse({'state': 200})


class UserApplyFourView(View):
    def get(self, request):
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        return render(request, 'user/apply-3.html', {'user': user})
