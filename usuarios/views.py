from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from usuarios.forms import FormularioRegistro, FormularioEdicionPerfil
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario

# Create your views here.
def login_usuarios(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            
            usuario = formulario.get_user()

            login(request, usuario)

            Usuario.objects.get_or_create(user=usuario)  # Crea un objeto Usuario si no existe
            
            return redirect('inicio')
    else:
        formulario = AuthenticationForm()

    return render(request, 'usuarios/login.html', {'formulario':formulario})

def registro_usuarios(request):
    
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('login')
    else:
        formulario = FormularioRegistro()

    return render(request, 'usuarios/registro.html', {'formulario':formulario})

@login_required
def ver_perfil(request):
    perfil, created = Usuario.objects.get_or_create(user=request.user)
    user = request.user
    return render(request, 'usuarios/ver_perfil.html', {'perfil': perfil, 'user': user})


@login_required
def editar_perfil(request):
    
    usuario, created = Usuario.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        formulario = FormularioEdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():

            # Guardamos primero los campos del modelo User
            formulario.save()
        
            # Ahora actualizamos y guardamos los campos del modelo Usuario
            if formulario.cleaned_data.get('avatar'):
                # Si se subió un nuevo avatar, lo guardamos
                usuario.avatar = formulario.cleaned_data.get('avatar')
            if formulario.cleaned_data.get('fecha_nacimiento'):
                # Si se subió una nueva fecha de nacimiento, la guardamos
                usuario.fecha_nacimiento = formulario.cleaned_data.get('fecha_nacimiento')
            if formulario.cleaned_data.get('sede_asignada'):
                # Si se subió una nueva sede asignada, la guardamos
                usuario.sede_asignada = formulario.cleaned_data.get('sede_asignada')

            usuario.save()
        
        # Redirigimos a la vista de perfil    
        return redirect('ver_perfil')
    
    else:
        formulario = FormularioEdicionPerfil(
        initial={
            'avatar': usuario.avatar,
            'fecha_nacimiento': usuario.fecha_nacimiento,
            'sede_asignada': usuario.sede_asignada,
        },
        instance=request.user
    )

    return render(request, 'usuarios/editar_perfil.html', {'formulario':formulario})