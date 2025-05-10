from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sede_asignada = models.CharField(max_length=100, null=True, blank=True)