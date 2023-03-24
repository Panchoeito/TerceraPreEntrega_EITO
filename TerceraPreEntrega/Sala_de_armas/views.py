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

def registro(request):
    if request.method == 'POST':
        
        formularioRegistro = Registro(request.POST)
        print(formularioRegistro)
        
        if formularioRegistro.is_valid:
        
            informacion = formularioRegistro.cleaned_data

            usuario = Usuarios(nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"])
            usuario.save()
            return render(request, 'Sala_de_armas/registro.html')
        else:
            formularioRegistro = Registro()
        
    return render(request, 'Sala_de_armas/registro.html', {"formularioRegistro": formularioRegistro})
    
def registrofusil(request):
    if request.method == 'POST':
        
        formularioRegistrofusil = Registrofusil(request.POST)
        print(formularioRegistrofusil)
        
        if formularioRegistrofusil.is_valid:
        
            informacion = formularioRegistrofusil.cleaned_data

            fusil = Fusile(tipo=informacion["tipo"], ni=informacion["ni"])
            fusil.save()
            return render(request, 'Sala_de_armas/registro.html')
        else:
            formularioRegistrofusil = Registrofusil()
        
    return render(request, 'Sala_de_armas/registro.html', {"formularioRegistrofusil": formularioRegistrofusil})
    
def registromunicion(request):
    if request.method == 'POST':
        
        formularioRegistromunicion = Registromunicion(request.POST)
        print(formularioRegistromunicion)
        
        if formularioRegistromunicion.is_valid:
        
            informacion = formularioRegistromunicion.cleaned_data

            municion = Municion(calibre=informacion["calibre"], cantidad=informacion["cantidad"])
            municion.save()
            return render(request, 'Sala_de_armas/registro.html')
        else:
            formularioRegistromunicion = Registromunicion()
        
    return render(request, 'Sala_de_armas/registro.html', {"formularioRegistromunicion": formularioRegistromunicion})

def registrousuario(request):
    return render(request, 'Sala_de_armas/registrousuario.html')

def consulta(request):
    return render(request, 'Sala_de_armas/consulta.html')