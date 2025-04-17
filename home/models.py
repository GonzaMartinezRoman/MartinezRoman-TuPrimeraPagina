from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    edad= models.CharField(max_length=3)
    sede_inscripcion = models.CharField(max_length=100)