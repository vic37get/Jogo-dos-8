from django.urls import path
from . import views

app_name = 'jogoApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('escolha', views.executaBusca, name='escolha'),
]
