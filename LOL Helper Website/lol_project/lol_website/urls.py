from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('champions/', views.champions, name='champions'),
    re_path(r'^champions/(?P<champion_name>[a-zA-Z]+)/$', views.champion_detail, name='champion_detail'),
]
