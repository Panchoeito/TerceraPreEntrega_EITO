from django.shortcuts import render
from django.http import HttpResponse
from django.http import request
from Sala_de_armas.forms import Registro, Registrofusil, Registromunicion
from Sala_de_armas.models import Usuarios, Fusile, Municion


# Create your views here.
def padre(request):
    return render(request, 'Sala_de_armas/padre.html')

def index(request):
    return render(request, 'Sala_de_armas/index.html')

def registrousuarios(request):
    return render(request, 'Sala_de_armas/registrousuario.html')

def consulta(request):
    return render(request, 'Sala_de_armas/consulta.html')