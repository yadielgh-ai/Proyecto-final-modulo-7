# gestion/models.py
from django.db import models

# Se define el modelo que representa a los clientes del sistema
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre

# Se define el modelo para las cuentas bancarias o billeteras
class Cuenta(models.Model):
    # Se establece una relación "Muchos a Uno": Un cliente puede tener varias cuentas, 
    # pero una cuenta pertenece a un solo cliente.
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Cuenta {self.id} - {self.cliente.nombre}"

# Se define el modelo para registrar los movimientos de dinero
class Transaccion(models.Model):
    # Se asocia cada transacción a una cuenta específica
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    # Se almacena el tipo de operación (ej. 'Depósito', 'Retiro', 'Transferencia')
    tipo = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    # Se guarda automáticamente la fecha y hora en que se crea el registro
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} de ${self.monto} en Cuenta {self.cuenta.id}"