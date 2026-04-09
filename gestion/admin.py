from django.contrib import admin
from .models import Cliente, Cuenta, Transaccion

# Personalización del modelo Cliente según la pauta
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')

# Registramos el cliente con su personalización
admin.site.register(Cliente, ClienteAdmin)
# Registramos el resto normalmente
admin.site.register(Cuenta)
admin.site.register(Transaccion)