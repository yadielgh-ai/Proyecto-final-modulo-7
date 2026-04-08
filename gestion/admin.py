from django.contrib import admin
# Se importan los modelos creados previamente
from .models import Cliente, Cuenta, Transaccion

# Se registra el modelo Cliente en el panel de administración para su gestión
admin.site.register(Cliente)

# Se registra el modelo Cuenta en el panel de administración
admin.site.register(Cuenta)

# Se registra el modelo Transaccion en el panel de administración
admin.site.register(Transaccion)