from django.shortcuts import render

# Create your views here.
def login_usuarios(request):
    return render(request, 'usuarios/login.html')