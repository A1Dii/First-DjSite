from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('hltv/', views.hltv, name = 'HLTV'),
    path('Faceit/', views.Faceit, name='Faceit'),
    path('blast/', views.blast, name='BLAST')
]