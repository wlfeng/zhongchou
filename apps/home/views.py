from django.shortcuts import render
from django.views.generic import View

from apps.project.models import ProjectListModels
from apps.user.models import UserModels
from .models import BannerModels, TitleIconModel


class IndexView(View):
    def get(self, request):
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        property = ProjectListModels.objects.all()
        property_kj = property.filter(type='kj')[:4]
        property_sj = property.filter(type='sj')[:4]
        property_ny = property.filter(type='ny')[:4]
        property_qt = property.all()[:4]
        banner = BannerModels.objects.all()
        title_icon = TitleIconModel.objects.all()[:3]
        return render(request, 'home/index.html',
                      {'property_kj': property_kj, 'property_sj': property_sj, 'property_ny': property_ny,
                       'property_qt': property_qt, 'banner': banner, 'title_icon': title_icon, 'user': user})
