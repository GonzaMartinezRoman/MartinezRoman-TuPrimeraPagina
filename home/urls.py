from django.urls import path
from home.views import inicio, crear_registro  # Importa las vistas de la app 'home'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('registros/crear', crear_registro, name="crear_registro"),
]