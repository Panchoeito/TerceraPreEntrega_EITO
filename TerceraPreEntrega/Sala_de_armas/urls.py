
from django.urls import path
from Sala_de_armas.views import *

urlpatterns = [
    path('padre/', padre, name='Padre'),
    path('', index, name='Inicio'),
    path('registro-usuario/', registrousuarios, name='registrousuarios'),
    path('registro-fusil/', registrofusiles, name='registrofusiles'),
    path('registro-municion/', registromunicion, name='registromunicion'),
]
