from django.contrib import admin
from home.models import Cliente

# Register your models here.
admin.site.site_header = "Gestión de clientes de Gimnasios Training-Center" # Le coloco un título a la página de administración
admin.site.register(Cliente)