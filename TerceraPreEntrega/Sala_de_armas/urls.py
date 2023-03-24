
from django.urls import path
from Sala_de_armas.views import *

urlpatterns = [
    path('padre/', padre, name='Padre'),
    path('', index, name='Inicio'),
    path('registrousuario/', registrousuario, name='registrousuario'),
]
