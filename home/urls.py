from django.urls import path
from home.views import inicio, crear_registro, listado_de_clientes, FichaCliente  # Importa las vistas de la app 'home'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('registros/', listado_de_clientes, name="listado_de_clientes"), # Clase en formato vista
    path('registros/crear', crear_registro, name="crear_registro"), # Clase en formato vista
    path('registros/<int:pk>', FichaCliente.as_view(), name="detalles_registro"), # Clase basada en vista
    # path('registros/eliminar', , name="eliminar_registro"), # Clase basada en vista
    # path('registros/modificar', , name="modificar_registro"), # Clase basada en vista
    
]