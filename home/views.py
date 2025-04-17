from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'home/inicio.html')

def crear_registro(request):
    return render(request, 'home/crear_registro.html')