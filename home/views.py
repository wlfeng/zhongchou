from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from project.models import ProjectListModels


class IndexView(View):
    def get(self, request):
        property = ProjectListModels.objects.all()
        property_kj = property.filter(type='kj')[:4]
        property_sj = property.filter(type='sj')[:4]
        property_ny = property.filter(type='ny')[:4]
        property_qt = property.all()[:4]
        return render(request, 'home/index.html',
                      {'property_kj': property_kj, 'property_sj': property_sj, 'property_ny': property_ny,
                       'property_qt': property_qt})
