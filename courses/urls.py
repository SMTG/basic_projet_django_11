from django.conf.urls import url
#from  django.contrib.auth import views as vue_auth
from . import views


urlpatterns = [
    # dashboard
   # url(r'^$', views.dashboard, name='dashboard'),
   # url(r'^register/$', views.register, name='register'),
    url(r'^home/$', views.home, name='home'),
]