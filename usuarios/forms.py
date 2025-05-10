from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', max_length=150, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}  # Elimina los textos de ayuda
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Repetir contraseña'}),
        }

class FormularioEdicionPerfil(UserChangeForm):
    password = None  # Evita que se muestre el campo de contraseña
    email = forms.EmailField(label='Correo electrónico', required=True)
    username = forms.CharField(label='Nombre de usuario', max_length=150, required=True)
    first_name = forms.CharField(label='Nombre', max_length=30, required=False)
    last_name = forms.CharField(label='Apellido', max_length=150, required=False)
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    avatar = forms.ImageField(label='Avatar', required=False, widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))
    sede_asignada = forms.CharField(label='Sede asignada', max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Ej. Constituyentes'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'fecha_nacimiento', 'avatar']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'fecha_nacimiento': forms.DateInput(attrs={'placeholder': 'Fecha de nacimiento', 'type': 'date'}),
            'avatar': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }