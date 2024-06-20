from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blast/', views.blast, name='blast'),
    path('faceit/', views.faceit, name='faceit'),
    path('hltv/', views.hltv, name='hltv')
]