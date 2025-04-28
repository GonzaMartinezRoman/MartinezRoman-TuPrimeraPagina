from django.shortcuts import render, redirect
#from django.http import HttpResponse
from home.forms import RegistrarCliente
from home.models import Cliente

# Create your views here.

def inicio(request):
    return render(request, 'home/inicio.html')

def crear_registro(request):

    if request.method == 'POST':
        formulario = RegistrarCliente(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            cliente = Cliente(nombre=info['nombre'], apellido=info['apellido'], email=info['email'], edad=info['edad'], fecha_de_nacimiento=info['fecha_de_nacimiento'], sede_inscripcion=info['sede_inscripcion'])
            cliente.save()
            
            # Después de guardar el cliente me voy a Inicio.
            return redirect('listado_de_clientes')
    else:
        formulario = RegistrarCliente()

    return render(request, 'home/crear_registro.html', {'formulario':formulario})

def listado_de_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'home/listado_de_clientes.html', {'clientes':clientes})