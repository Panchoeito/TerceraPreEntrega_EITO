from django import forms


class RegistrousuarioForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni = forms.IntegerField()

class RegistrofusilForm(forms.Form):
    tipo = forms.CharField(max_length=20)
    ni = forms.IntegerField()

class RegistromunicionForm(forms.Form):
    calibre = forms.CharField(max_length=20)
    cantidad = forms.IntegerField()
    
class ConsultausuarioForm(forms.Form):
    dni = forms.IntegerField()