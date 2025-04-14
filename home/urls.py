from django.urls import path
from home.views import inicio  # Importa la vista 'inicio' de la app 'home'

urlpatterns = [
    path('', inicio, name='inicio'),  # URL para la vista de inicio
]