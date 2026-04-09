# gestion/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
# Se importan funciones de agregación para consultas avanzadas del ORM
from django.db.models import Sum, Count
from .models import Cliente, Cuenta, Transaccion
# Se importa el Mixin de seguridad desde la aplicación preinstalada 'auth'
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cliente, Cuenta, Transaccion

# Se define la vista para listar todos los clientes (Read)
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    # CORRECCIÓN: Se ajusta la ruta para que apunte a la carpeta 'gestion'
    template_name = 'gestion/cliente_list.html'
    context_object_name = 'clientes'

# Se define la vista para crear un nuevo cliente (Create)
class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono']
    # CORRECCIÓN: Se ajusta la ruta para que apunte a la carpeta 'gestion'
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

# Se define la vista para actualizar un cliente existente (Update)
class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono']
    # CORRECCIÓN: Se ajusta la ruta para que apunte a la carpeta 'gestion'
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

# Se define la vista para eliminar un cliente (Delete)
class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    # CORRECCIÓN: Se ajusta la ruta para que apunte a la carpeta 'gestion'
    template_name = 'gestion/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')


# --- CRUD PARA CUENTAS ---

# Se define la vista para listar cuentas
class CuentaListView(LoginRequiredMixin, ListView):
    model = Cuenta
    template_name = 'gestion/cuenta_list.html'
    context_object_name = 'cuentas'

# Se define la vista para crear una cuenta
class CuentaCreateView(LoginRequiredMixin, CreateView):
    model = Cuenta
    # Se omiten campos automáticos; el usuario elige el cliente y el saldo inicial
    fields = ['cliente', 'saldo']
    template_name = 'gestion/cuenta_form.html'
    success_url = reverse_lazy('cuenta_list')

# Se define la vista para editar una cuenta
class CuentaUpdateView(LoginRequiredMixin, UpdateView):
    model = Cuenta
    fields = ['cliente', 'saldo']
    template_name = 'gestion/cuenta_form.html'
    success_url = reverse_lazy('cuenta_list')

# Se define la vista para eliminar una cuenta
class CuentaDeleteView(LoginRequiredMixin, DeleteView):
    model = Cuenta
    template_name = 'gestion/cuenta_confirm_delete.html'
    success_url = reverse_lazy('cuenta_list')


# --- CRUD PARA TRANSACCIONES ---

# Se define la vista para listar transacciones
class TransaccionListView(LoginRequiredMixin, ListView):
    model = Transaccion
    template_name = 'gestion/transaccion_list.html'
    context_object_name = 'transacciones'

# Se define la vista para registrar una transacción
class TransaccionCreateView(LoginRequiredMixin, CreateView):
    model = Transaccion
    # La fecha se genera automáticamente, por lo que no se incluye en el formulario
    fields = ['cuenta', 'tipo', 'monto']
    template_name = 'gestion/transaccion_form.html'
    success_url = reverse_lazy('transaccion_list')

# Se define la vista para editar una transacción
class TransaccionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaccion
    fields = ['cuenta', 'tipo', 'monto']
    template_name = 'gestion/transaccion_form.html'
    success_url = reverse_lazy('transaccion_list')

# Se define la vista para eliminar una transacción
class TransaccionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaccion
    template_name = 'gestion/transaccion_confirm_delete.html'
    success_url = reverse_lazy('transaccion_list')

# Se define una vista basada en TemplateView para mostrar reportes combinados
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'gestion/dashboard.html'

    def get_context_data(self, **kwargs):
        # Se obtiene el contexto base de la clase padre
        context = super().get_context_data(**kwargs)
        
        # 1. ORM Avanzado (Anotaciones): 
        # Se anexa a cada cliente el número total de sus cuentas y la suma de sus saldos
        context['clientes_resumen'] = Cliente.objects.annotate(
            num_cuentas=Count('cuenta'),
            saldo_total=Sum('cuenta__saldo')
        )

        # 2. Consulta SQL Personalizada usando raw():
        # Se ejecuta una consulta directa a la base de datos MySQL. 
        # Django nombra las tablas automáticamente como "nombre_app_nombre_modelo"
        consulta_sql = "SELECT id, nombre, email FROM gestion_cliente ORDER BY id DESC LIMIT 5"
        context['ultimos_clientes_sql'] = Cliente.objects.raw(consulta_sql)

        return context