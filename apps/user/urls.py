from django.conf.urls import url
from .views import LoginView, RegisterView, UserdetailView, MyProjectView, UserAuthView, UserApplyOneView, \
    UserApplyTwoView, UserApplyThreeView, UserApplyFourView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register', RegisterView.as_view(), name='register'),
    url(r'^user_detail', UserdetailView.as_view(), name='user_detail'),
    url(r'^my_project', MyProjectView.as_view(), name='my_project'),
    url(r'^userauth', UserAuthView.as_view(), name='userauth'),
    url(r'^userapply_one', UserApplyOneView.as_view(), name='userapply_one'),
    url(r'^userapply_two', UserApplyTwoView.as_view(), name='userapply_two'),
    url(r'^userapply_three', UserApplyThreeView.as_view(), name='userapply_three'),
    url(r'^userapply_four', UserApplyFourView.as_view(), name='userapply_four'),

]
