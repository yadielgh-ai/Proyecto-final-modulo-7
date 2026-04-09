# gestion/urls.py
from django.urls import path
from .views import (
    ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
    CuentaListView, CuentaCreateView, CuentaUpdateView, CuentaDeleteView,
    TransaccionListView, TransaccionCreateView, TransaccionUpdateView, TransaccionDeleteView
)

urlpatterns = [
    # --- Rutas de Clientes ---
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/nuevo/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),

    # --- Rutas de Cuentas ---
    path('cuentas/', CuentaListView.as_view(), name='cuenta_list'),
    path('cuentas/nueva/', CuentaCreateView.as_view(), name='cuenta_create'),
    path('cuentas/editar/<int:pk>/', CuentaUpdateView.as_view(), name='cuenta_update'),
    path('cuentas/eliminar/<int:pk>/', CuentaDeleteView.as_view(), name='cuenta_delete'),

    # --- Rutas de Transacciones ---
    path('transacciones/', TransaccionListView.as_view(), name='transaccion_list'),
    path('transacciones/nueva/', TransaccionCreateView.as_view(), name='transaccion_create'),
    path('transacciones/editar/<int:pk>/', TransaccionUpdateView.as_view(), name='transaccion_update'),
    path('transacciones/eliminar/<int:pk>/', TransaccionDeleteView.as_view(), name='transaccion_delete'),
]