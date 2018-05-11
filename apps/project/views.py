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

m_sort_type = ''
m_sort_state = ''
m_sort_money = ''


class ProjectListView(View):
    def get(self, request):
        global m_sort_type, m_sort_state, m_sort_money
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
                       })

    def post(self, request):
        text = request.POST.get('val')

        property = ProjectListModels.objects.filter(Q(title__contains=text) | Q(introduce__contains=text))
        property = pager(request, property)
        return render(request, 'project/projects.html',
                      {'property': property})


def pager(request, property):
    try:
        page = request.GET.get('page', 1)
    except:
        page = 1

    p = Paginator(property, 12, request=request)

    property = p.page(page)
    return property


class ProjectDetailView(View):
    def get(self, request, id):
        project = ProjectListModels.objects.get(id=id)
        money = project.moneymodels_set.all()
        print(type(money[0].is_quantity))
        return render(request, 'project/project.html', {'project': project, 'money': money})


class PayStepOneView(View):
    def get(self, request, mon_id):
        money = MoneyModels.objects.get(id=mon_id)
        return render(request, 'project/pay-step-1.html', {'money': money})


class PayStepTwoView(View):
    def get(self, request, mon_id):
        address = ''
        money = MoneyModels.objects.get(id=mon_id)
        if request.session.has_key('islogin'):
            user = UserModels.objects.get(id=request.session['user_id'])
            address = user.addressmodels_set.all()
        return render(request, 'project/pay-step-2.html', {'money': money, 'mon_id': mon_id, 'address': address})

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
