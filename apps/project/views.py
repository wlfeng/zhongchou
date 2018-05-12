from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from django.views.generic import View
from pure_pagination import Paginator
from django.http import JsonResponse
from apps.user.models import UserModels, AddressModels
from utils.islogin import login_required
from .models import ProjectListModels, MoneyModels
from django.core.urlresolvers import reverse
from apps.user.models import FollowModels

m_sort_type = ''
m_sort_state = ''
m_sort_money = ''


def pager(request, property):
    try:
        page = request.GET.get('page', 1)
    except:
        page = 1

    p = Paginator(property, 12, request=request)

    property = p.page(page)
    return property


class ProjectListView(View):
    def get(self, request):
        global m_sort_type, m_sort_state, m_sort_money
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        property = ProjectListModels.objects.all()
        size = property.count()
        sort_type = request.GET.get('sort_type', 'null')
        sort_state = request.GET.get('sort_state', 'null')
        sort_money = request.GET.get('sort_money', 'null')

        if sort_type == 'null':
            sort_type = m_sort_type
        else:
            m_sort_type = property
            if sort_type:
                property = property.filter(type=sort_type)

        if sort_state == 'null':
            sort_state = m_sort_state
        else:
            m_sort_state = sort_state
            if sort_state:
                property = property.filter(state=sort_state)

        if sort_money == 'null':
            sort_money = m_sort_money
        else:
            m_sort_money = sort_money
            if sort_money:
                property = property.order_by(sort_money)

        property = pager(request, property)
        return render(request, 'project/projects.html',
                      {'property': property, 'size': size, 'sort_type': sort_type, 'sort_state': sort_state,
                       'sort_money': sort_money,
                       'm_sort_type': m_sort_type, 'm_sort_state': m_sort_state, 'm_sort_money': m_sort_money
                          , 'user': user})

    def post(self, request):
        text = request.POST.get('val')
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        property = ProjectListModels.objects.filter(Q(title__contains=text) | Q(introduce__contains=text))
        property = pager(request, property)
        return render(request, 'project/projects.html',
                      {'property': property, 'user': user})


class ProjectDetailView(View):
    def get(self, request, id):
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        project = ProjectListModels.objects.get(id=id)
        money = project.moneymodels_set.all()
        return render(request, 'project/project.html', {'project': project, 'money': money, 'user': user})

    def post(self, request, id):

        try:
            pro = ProjectListModels.objects.get(id=id)
            # FollowModels.objects.get(project=pro, user=UserModels.objects.get(id=request.session['user_id']))
            fol = FollowModels()
            fol.project = pro
            fol.user = UserModels.objects.get(id=request.session['user_id'])
            fol.save()
            pro.flow_num += 1
            pro.save()
            return JsonResponse({'status': '200'})
        except:
            return JsonResponse({'status': '500'})


class PayStepOneView(View):
    def get(self, request, mon_id):
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        money = MoneyModels.objects.get(id=mon_id)
        return render(request, 'project/pay-step-1.html', {'money': money, 'user': user})


class PayStepTwoView(View):
    def get(self, request, mon_id):
        try:
            user = UserModels.objects.get(id=request.session['user_id'])
        except:
            user = 'None'
        address = ''
        money = MoneyModels.objects.get(id=mon_id)
        if request.session.has_key('islogin'):
            user = UserModels.objects.get(id=request.session['user_id'])
            address = user.addressmodels_set.all()
        return render(request, 'project/pay-step-2.html',
                      {'money': money, 'mon_id': mon_id, 'address': address, 'user': user})

    def post(self, request, mon_id):

        phone = request.POST.get('phone')
        username = request.POST.get('username')
        p_address = request.POST.get('address')
        user = UserModels.objects.get(id=request.session['user_id'])
        address = AddressModels()
        address.user = user
        address.name = username
        address.phone = phone
        address.address = p_address
        address.save()
        return JsonResponse({'state': 'ok'})
