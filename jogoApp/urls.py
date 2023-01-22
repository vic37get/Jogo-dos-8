from django.urls import path
from . import views

app_name = 'jogoApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('buscaEmLargura', views.buscaEmLargura, name='buscaEmLargura'),
    path('buscaEmProfundidade', views.buscaEmProfundidade, name='buscaEmProfundidade'),
]