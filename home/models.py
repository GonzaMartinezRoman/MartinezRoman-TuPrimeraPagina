from django.db import models
import os

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    edad = models.IntegerField(max_length=3)
    fecha_de_nacimiento = models.DateField(null=True)
    sede_inscripcion = models.CharField(max_length=100)
    foto_carnet = models.ImageField(upload_to='fotos_carnet/', null=True, blank=True)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
    # def __str__(self):
    #     return f'Nombre: {self.nombre},  Apellido: {self.apellido}, Email:  {self.email}, Edad: {self.edad}, Fecha de nacimiento: {self.fecha_de_nacimiento}, Inscripto en sede: {self.sede_inscripcion}'

    def delete(self, *args, **kwargs):
        if self.foto_carnet:
            if os.path.isfile(self.foto_carnet.path):
                os.remove(self.foto_carnet.path)
        super().delete(*args, **kwargs)