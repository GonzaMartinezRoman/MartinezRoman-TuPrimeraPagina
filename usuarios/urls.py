from django.urls import path
from usuarios.views import login_usuarios
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_usuarios, name="login"),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name="logout"),
]