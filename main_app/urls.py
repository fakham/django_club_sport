from django.conf.urls import url
from . import views

urlpatterns = [
    url('inscription', views.inscription, name='inscription'),
    url('confirmation', views.confirmation, name='confirmation'),
    url('', views.index, name='index'),
]
