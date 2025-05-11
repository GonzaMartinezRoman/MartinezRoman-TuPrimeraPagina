from django.shortcuts import render, redirect
#from django.http import HttpResponse
from home.forms import RegistrarCliente
from home.models import Cliente
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, 'home/inicio.html')

def acerca_de_mi(request):
    return render(request, 'home/acerca_de_mi.html')

@login_required
def crear_cliente(request):
    if request.method == 'POST':
        formulario = RegistrarCliente(request.POST, request.FILES)  # Coloco el request.FILES para poder guardar la imagen
        if formulario.is_valid():
            info = formulario.cleaned_data
            cliente = Cliente(
                nombre=info['nombre'],
                apellido=info['apellido'],
                email=info['email'],
                edad=info['edad'],
                fecha_de_nacimiento=info['fecha_de_nacimiento'],
                sede_inscripcion=info['sede_inscripcion'],
                foto_carnet=info.get('foto_carnet')  # Guardar imagen
            )
            cliente.save()
            return redirect('listado_de_clientes')
    else:
        formulario = RegistrarCliente()

    return render(request, 'home/crear_cliente.html', {'formulario': formulario})

@login_required
def listado_de_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'home/listado_de_clientes.html', {'clientes':clientes})

# Clases basadas en vista
class FichaCliente(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'home/detalles_cliente.html'

class ModificarCliente(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'home/modificar_cliente.html'
    fields = ['nombre', 'apellido', 'email', 'edad', 'fecha_de_nacimiento', 'sede_inscripcion', 'foto_carnet']

    def get_success_url(self):
        return reverse_lazy('detalles_cliente', kwargs={'pk': self.object.pk})

class EliminarCliente(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'home/eliminar_cliente.html'
    success_url = reverse_lazy('listado_de_clientes')