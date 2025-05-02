from django.urls import path
from home.views import inicio, crear_cliente, listado_de_clientes, FichaCliente  # Importa las vistas de la app 'home'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('clientes/', listado_de_clientes, name="listado_de_clientes"), # Clase en formato vista
    path('clientes/crear', crear_cliente, name="crear_cliente"), # Clase en formato vista
    path('clientes/<int:pk>', FichaCliente.as_view(), name="detalles_cliente"), # Clase basada en vista
    # path('registros/eliminar', , name="eliminar_registro"), # Clase basada en vista
    # path('registros/modificar', , name="modificar_registro"), # Clase basada en vista
    
]