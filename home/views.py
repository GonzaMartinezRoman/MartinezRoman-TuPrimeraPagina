from django.shortcuts import render, redirect
#from django.http import HttpResponse
from home.forms import RegistrarCliente
from home.models import Cliente
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):
    return render(request, 'home/inicio.html')

def crear_cliente(request):

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

    return render(request, 'home/crear_cliente.html', {'formulario':formulario})

def listado_de_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'home/listado_de_clientes.html', {'clientes':clientes})

# Clases basadas en vista
class FichaCliente(DetailView):
    model = Cliente
    template_name = 'home/detalles_cliente.html'

class ModificarCliente(UpdateView):
    model = Cliente
    template_name = 'home/modificar_cliente.html'
    fields = ['nombre', 'apellido', 'email', 'edad', 'fecha_de_nacimiento', 'sede_inscripcion']
    success_url = reverse_lazy('listado_de_clientes')