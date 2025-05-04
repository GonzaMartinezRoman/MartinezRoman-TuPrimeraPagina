from django.urls import path
from home.views import inicio, acerca_de_mi, crear_cliente, listado_de_clientes, FichaCliente, ModificarCliente, EliminarCliente  # Importa las vistas de la app 'home'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('home/acerca-de-mi', acerca_de_mi, name="acerca_de_mi"), # Clase en formato vista
    path('clientes/', listado_de_clientes, name="listado_de_clientes"), # Clase en formato vista
    path('clientes/crear', crear_cliente, name="crear_cliente"), # Clase en formato vista
    path('clientes/<int:pk>', FichaCliente.as_view(), name="detalles_cliente"), # Clase basada en vista
    path('clientes/<int:pk>/modificar-cliente', ModificarCliente.as_view() , name="modificar_cliente"), # Clase basada en vista
    path('clientes/<int:pk>/eliminar-cliente', EliminarCliente.as_view() , name="eliminar_cliente"), # Clase basada en vista
]