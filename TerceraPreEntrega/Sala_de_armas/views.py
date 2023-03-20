from django.shortcuts import render
from django.http import HttpResponse
from django.http import request

# Create your views here.
def index(request):
    return render(request, 'Sala_de_armas/index.html')

def registro(request):
    return render(request, 'Sala_de_armas/registro.html')

def consulta(request):
    return render(request, 'Sala_de_armas/consulta.html')