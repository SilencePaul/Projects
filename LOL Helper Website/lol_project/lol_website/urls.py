from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('champions/', views.champions, name='champions'),
]
