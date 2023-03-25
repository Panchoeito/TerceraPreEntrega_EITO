from django.shortcuts import render
from django.http import HttpResponse
from django.http import request
from Sala_de_armas.forms import RegistrousuarioForm, RegistrofusilForm, RegistromunicionForm
from Sala_de_armas.models import Usuarios, Fusile, Municion


# Create your views here.
def padre(request):
    return render(request, 'Sala_de_armas/padre.html')

def index(request):
    return render(request, 'Sala_de_armas/index.html')

def registrousuarios(request):

    if request.method == "POST":
        formularioUsuario = RegistrousuarioForm(request.POST)
        print(formularioUsuario)
        
        if formularioUsuario.is_valid:
            registro = formularioUsuario.cleaned_data
            print(registro)
            usuario = Usuarios(nombre=registro["nombre"], apellido=registro["apellido"], dni=registro["dni"])
            usuario.save()
        
    return render(request, 'Sala_de_armas/registrousuario.html')

def registrofusiles(request):

    if request.method == "POST":
        formularioFusiles = RegistrofusilForm(request.POST)
        print(formularioFusiles)
        
        if formularioFusiles.is_valid:
            registro = formularioFusiles.cleaned_data
            print(registro)
            fusil = Fusile(tipo=registro["tipo"], ni=registro["ni"])
            fusil.save()

    return render(request, 'Sala_de_armas/registrofusiles.html')

def registromunicion(request):
    
    if request.method == "POST":
        formularioMunicion = RegistromunicionForm(request.POST)
        print(formularioMunicion)
        
        if formularioMunicion.is_valid:
            registro = formularioMunicion.cleaned_data
            print(registro)
            municion = Municion(calibre=registro["calibre"], cantidad=registro["cantidad"])
            municion.save()
        
    return render(request, 'Sala_de_armas/registromunicion.html')

def consulta(request):
    
    
    
    return render(request, 'Sala_de_armas/consulta.html')