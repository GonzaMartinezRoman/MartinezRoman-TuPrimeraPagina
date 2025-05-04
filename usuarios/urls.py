from django.urls import path
from usuarios.views import login_usuarios

urlpatterns = [
    path('login/', login_usuarios, name="login"),
    
]