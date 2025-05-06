from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
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
def editar_perfil(request):
    
    usuario, created = Usuario.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        formulario = FormularioEdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():

            if formulario.cleaned_data.get('avatar'):
                # Si se subió un nuevo avatar, lo guardamos
                usuario.avatar = formulario.cleaned_data['avatar']
            
            usuario.save()
            
            formulario.save()
            
            return redirect('inicio')
    else:
        formulario = FormularioEdicionPerfil(initial={'avatar':usuario.avatar},instance=request.user)

    return render(request, 'usuarios/editar_perfil.html', {'formulario':formulario})