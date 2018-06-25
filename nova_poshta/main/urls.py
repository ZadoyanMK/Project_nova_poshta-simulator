from django.conf.urls import url, include
from main import views


urlpatterns = [
    url(r'^add_order$', views.OrderFormView.as_view(), name='form-order'),
    url(r'^$', views.MainFormView.as_view(), name='form-main'),
    url(r'^', include('accounts.urls')),
    url(r'^to_main$', views.to_main, name='to-main'),
]
