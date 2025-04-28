from django import forms

class RegistrarCliente(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    email = forms.EmailField(label='Email')
    edad = forms.CharField(label='Edad', max_length=3)
    fecha_de_nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput(attrs={'type': 'date'}))  
    sede_inscripcion = forms.CharField(label='Sede de Inscripción', max_length=100)