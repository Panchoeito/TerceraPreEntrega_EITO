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
    
    if request.method == "POST":
        print(f"{request.POST}")
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        dni = request.POST["dni"]
        usuario = Usuarios(nombre=nombre, apellido=apellido, dni=dni)
        usuario.save()
        
    return render(request, 'Sala_de_armas/registrousuario.html')

def registrofusiles(request):
    
    if request.method == "POST":
        print(f"{request.POST}")
        tipo = request.POST["tipo"]
        ni = request.POST["ni"]
        fusil = Fusile(tipo=tipo, ni=ni)
        fusil.save()
        
    return render(request, 'Sala_de_armas/registrofusiles.html')

def registromunicion(request):
    
    if request.method == "POST":
        print(f"{request.POST}")
        calibre = request.POST["calibre"]
        cantidad = request.POST["cantidad"]
        municion = Municion(calibre=calibre, municion=municion)
        municion.save()
        
    return render(request, 'Sala_de_armas/registromunicion.html')

def consulta(request):
    return render(request, 'Sala_de_armas/consulta.html')