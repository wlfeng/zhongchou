from django.conf.urls import url
from .views import ProjectListView

urlpatterns = [
    url(r'^projects_list/$', ProjectListView.as_view(), name='projects_list'),
]
