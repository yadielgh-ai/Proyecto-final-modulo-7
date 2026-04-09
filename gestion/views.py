# gestion/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente, Cuenta, Transaccion

# Se define la vista para listar todos los clientes (Read)
class ClienteListView(ListView):
    model = Cliente
    # CORRECCIÓN: Se ajusta la ruta para que apunte a la carpeta 'gestion'
    template_name = 'gestion/cliente_list.html'
    context_object_name = 'clientes'

# Se define la vista para crear un nuevo cliente (Create)
class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono']
    # CORRECCIÓN: Se ajusta la ruta para que apunte a la carpeta 'gestion'
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

# Se define la vista para actualizar un cliente existente (Update)
class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono']
    # CORRECCIÓN: Se ajusta la ruta para que apunte a la carpeta 'gestion'
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

# Se define la vista para eliminar un cliente (Delete)
class ClienteDeleteView(DeleteView):
    model = Cliente
    # CORRECCIÓN: Se ajusta la ruta para que apunte a la carpeta 'gestion'
    template_name = 'gestion/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')


# --- CRUD PARA CUENTAS ---

# Se define la vista para listar cuentas
class CuentaListView(ListView):
    model = Cuenta
    template_name = 'gestion/cuenta_list.html'
    context_object_name = 'cuentas'

# Se define la vista para crear una cuenta
class CuentaCreateView(CreateView):
    model = Cuenta
    # Se omiten campos automáticos; el usuario elige el cliente y el saldo inicial
    fields = ['cliente', 'saldo']
    template_name = 'gestion/cuenta_form.html'
    success_url = reverse_lazy('cuenta_list')

# Se define la vista para editar una cuenta
class CuentaUpdateView(UpdateView):
    model = Cuenta
    fields = ['cliente', 'saldo']
    template_name = 'gestion/cuenta_form.html'
    success_url = reverse_lazy('cuenta_list')

# Se define la vista para eliminar una cuenta
class CuentaDeleteView(DeleteView):
    model = Cuenta
    template_name = 'gestion/cuenta_confirm_delete.html'
    success_url = reverse_lazy('cuenta_list')


# --- CRUD PARA TRANSACCIONES ---

# Se define la vista para listar transacciones
class TransaccionListView(ListView):
    model = Transaccion
    template_name = 'gestion/transaccion_list.html'
    context_object_name = 'transacciones'

# Se define la vista para registrar una transacción
class TransaccionCreateView(CreateView):
    model = Transaccion
    # La fecha se genera automáticamente, por lo que no se incluye en el formulario
    fields = ['cuenta', 'tipo', 'monto']
    template_name = 'gestion/transaccion_form.html'
    success_url = reverse_lazy('transaccion_list')

# Se define la vista para editar una transacción
class TransaccionUpdateView(UpdateView):
    model = Transaccion
    fields = ['cuenta', 'tipo', 'monto']
    template_name = 'gestion/transaccion_form.html'
    success_url = reverse_lazy('transaccion_list')

# Se define la vista para eliminar una transacción
class TransaccionDeleteView(DeleteView):
    model = Transaccion
    template_name = 'gestion/transaccion_confirm_delete.html'
    success_url = reverse_lazy('transaccion_list')