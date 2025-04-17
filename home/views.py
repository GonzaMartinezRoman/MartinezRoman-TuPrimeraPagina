from django.shortcuts import render
from django.http import HttpResponse
from home.forms import RegistrarCliente

# Create your views here.

def inicio(request):
    return render(request, 'home/inicio.html')

def crear_registro(request):

    if request.method == 'POST':
        formulario = RegistrarCliente(request.POST)
    else:
        formulario = RegistrarCliente()

    return render(request, 'home/crear_registro.html', {'formulario':formulario})