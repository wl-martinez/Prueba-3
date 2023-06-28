from django.db import models
from django.forms import IntegerField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=500, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="img/", null=True, blank=True)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.nombre