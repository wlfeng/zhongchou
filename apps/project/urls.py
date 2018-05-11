from django.conf.urls import url
from .views import ProjectListView, ProjectDetailView, PayStepOneView, PayStepTwoView

urlpatterns = [
    url(r'^projects_list/$', ProjectListView.as_view(), name='projects_list'),
    url(r'^projects_detail/(?P<id>.*)$', ProjectDetailView.as_view(), name='projects_detail'),
    url(r'^pay_step_one/(?P<mon_id>.*)$', PayStepOneView.as_view(), name='pay_step_one'),
    url(r'^pay_step_two/(?P<mon_id>.*)$', PayStepTwoView.as_view(), name='pay_step_two')
]
