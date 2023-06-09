from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    
    def __str__(self):
        return f"{self.apellido} - {self.nombre} - {self.dni}"
    
class Fusile(models.Model):
    tipo = models.CharField(max_length=20)
    ni = models.IntegerField()
    
    def __str__(self):
        return f"{self.tipo} - {self.ni}"   
    
class Municion(models.Model):
    Calibre = models.CharField(max_length=20)
    Cantidad = models.IntegerField()
    
    def __str__(self):
        return f"{self.calibre} - {self.cantidad}"