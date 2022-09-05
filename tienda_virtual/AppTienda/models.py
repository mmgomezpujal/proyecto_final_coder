from urllib.parse import MAX_CACHE_SIZE
from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Distribuidores(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    direccion = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class PostVenta(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()
    fecha = models.DateField()
    producto = models.CharField(max_length=128)
    descripcion_reclamo = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.producto}'


# Create your models here.
