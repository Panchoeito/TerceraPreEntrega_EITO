from django import forms


class Registro(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()

class Registrofusil(forms.Form):
    tipo = forms.CharField()
    ni = forms.IntegerField()

class Registromunicion(forms.Form):
    calibre = forms.CharField()
    cantidad = forms.IntegerField()