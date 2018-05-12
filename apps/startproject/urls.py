from django.conf.urls import url
from .views import StartStepView, StartStepOneView, StartStepTwoView, StartStepThreeView, StartSteprFourView

urlpatterns = [
    url(r'^start_pro/$', StartStepView.as_view(), name='start_pro'),
    url(r'^start_pro_one/$', StartStepOneView.as_view(), name='start_pro_one'),
    url(r'^start_pro_two/$', StartStepTwoView.as_view(), name='start_pro_two'),
    url(r'^start_pro_three/$', StartStepThreeView.as_view(), name='start_pro_three'),
    url(r'^start_pro_four/$', StartSteprFourView.as_view(), name='start_pro_four'),
]
