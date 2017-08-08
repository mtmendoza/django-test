from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^getdata/', views.index)
]