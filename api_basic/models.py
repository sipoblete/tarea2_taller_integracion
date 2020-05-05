from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    nombre = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length = 200)

    def __str__(self):
        return self.nombre

class Hamburguesa(models.Model):
    nombre = models.CharField(max_length = 200)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 200)
    imagen = models.CharField(max_length = 200)
    ingredientes = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.nombre



