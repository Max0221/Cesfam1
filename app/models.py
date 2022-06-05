from django.db import models
from django.forms import BooleanField, EmailField

# Create your models here.
class medicamento(models.Model):
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField()
    fecha_fabricacion = models.DateField()
    caducado = models.BooleanField()
    
    def __str__(self):
        return self.nombre

class fichapaciente(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    numero = models.IntegerField()
    descripcion = models.TextField()
    medicamento = models.ForeignKey(medicamento, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class medicamentocompra(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre
        

    

