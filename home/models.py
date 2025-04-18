from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    edad= models.CharField(max_length=3)
    sede_inscripcion = models.CharField(max_length=100)

    def __str__(self):
        return f'Nombre: {self.nombre},  Apellido: {self.apellido}, Email:  {self.email}, Edad: {self.edad}, Inscripto en sede: {self.sede_inscripcion}'