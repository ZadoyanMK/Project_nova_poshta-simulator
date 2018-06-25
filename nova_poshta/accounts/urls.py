from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'login$', views.UserLoginView.as_view(), name='form-login'),
    url(r'reg$', views.UserCreateView.as_view(), name='form-registration'),
    url(r'logout$', views.logout_view, name='form-login'),
]
