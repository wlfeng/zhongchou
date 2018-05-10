from django.conf.urls import url
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    url(r'^projects_list/$', ProjectListView.as_view(), name='projects_list'),
    url(r'^projects_detail/(?P<id>.*)$', ProjectDetailView.as_view(), name='projects_detail'),
]
