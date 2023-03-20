
from django.urls import path
from Sala_de_armas.views import *

urlpatterns = [
    path('padre/', padre, name='Padre'),
    path('', index, name='Inicio'),
    path('registro/', registro, name='Registro'),
    path('consulta/', consulta, name='Consulta'),
]
