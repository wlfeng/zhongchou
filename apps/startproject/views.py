from django.core.files.storage import default_storage
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.views.generic import View
import time

from apps.project.models import ProjectListModels, CompanyModels
from zhongChou.settings import MEDIA_ROOT
from datetime import datetime
from datetime import timedelta


class StartStepView(View):
    def get(self, request):
        return render(request, 'startproject/start.html')


class StartStepOneView(View):
    def get(self, request):
        return render(request, 'startproject/start-step-1.html')


class StartStepTwoView(View):
    def get(self, request):
        return render(request, 'startproject/start-step-2.html')

    def post(self, request):
        # {
        #     'project_name': project_name,
        #     'project_money': project_money,
        #     'poeple_detail_name': poeple_detail_name,
        #     'poeple_name': poeple_name,
        #     'project_day': project_day,
        #     'service_phone': service_phone,
        #     'phone': phone,
        #     'project_msg': project_msg,
        #     'type': type
        # }
        print('00000')
        type = request.POST['type']
        project_name = request.POST['project_name']
        project_money = request.POST['project_money']
        project_day = request.POST['project_day']
        poeple_detail_name = request.POST['poeple_detail_name']
        poeple_name = request.POST['poeple_name']
        service_phone = request.POST['service_phone']
        image_title = save_image(str(int(time.time())) + request.FILES['image_title'].name,
                                 request.FILES['image_title'].name, 'project')
        image = save_image(str(int(time.time())) + request._files['image'].name,
                           request._files['image'].name, 'con_image')
        project_msg = request.POST['project_msg']
        people_image = save_image(str(int(time.time())) + request._files['people_image'].name,
                                  request._files['people_image'].name, 'company')
        now = datetime.now()
        aDay = timedelta(days=-project_day)
        now = now + aDay
        company = CompanyModels()
        company.name = poeple_name
        company.aut = '未认证'
        company.introduce = poeple_detail_name
        company.phone = service_phone
        company.image = people_image
        company.save()
        project = ProjectListModels()
        project.type = type
        project.title = project_name
        project.target_money = project_money
        project.image = image_title
        project.introduce = project_msg
        project.state = '未开始众筹'
        project.end_time = now.strftime('%Y-%m-%d')
        project.company = company
        project.image = image_title
        project.con_image = image
        return JsonResponse({'msg', 'ok'})


class StartStepThreeView(View):
    def get(self, request):
        return render(request, 'startproject/start-step-3.html')


class StartSteprFourView(View):
    def get(self, request):
        return render(request, 'startproject/start-step-4.html')


def save_image(image_detail_filename, file_obj, uploadimage_url):
    with default_storage.open(MEDIA_ROOT + '/' + uploadimage_url + '/' + image_detail_filename, 'wb+') as file:
        for chunk in file_obj.chunks():
            file.write(chunk)
    image_detail_upload = 'media/' + uploadimage_url + '/' + image_detail_filename
    return image_detail_upload
