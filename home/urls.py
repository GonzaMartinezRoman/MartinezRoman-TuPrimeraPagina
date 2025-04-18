from django.urls import path
from home.views import inicio, crear_registro, listado_de_clientes  # Importa las vistas de la app 'home'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('registros/', listado_de_clientes, name="listado_de_clientes"),
    path('registros/crear', crear_registro, name="crear_registro"),
]