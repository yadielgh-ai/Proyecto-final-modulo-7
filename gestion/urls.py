# gestion/urls.py
from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

# Se definen las rutas específicas para la aplicación de gestión
urlpatterns = [
    # Ruta para el listado de clientes
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    # Ruta para el formulario de creación
    path('clientes/nuevo/', ClienteCreateView.as_view(), name='cliente_create'),
    # Ruta para editar un cliente específico (se pasa el ID en la URL)
    path('clientes/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    # Ruta para eliminar un cliente específico
    path('clientes/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
]