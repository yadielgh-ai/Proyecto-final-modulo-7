# gestion/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente

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