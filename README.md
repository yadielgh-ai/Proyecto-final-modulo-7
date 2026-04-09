# Alke Wallet - Billetera Digital 💼

Este proyecto es una aplicación web desarrollada con Django para la gestión de activos financieros de una empresa fintech ficticia llamada "Alke Financial". Permite gestionar clientes, cuentas bancarias y registrar transacciones financieras.

## 🚀 Características Principales

* **Arquitectura MVC (MTV):** Implementación estructurada utilizando Modelos, Vistas Genéricas y Plantillas de Django.
* **Gestión de Base de Datos:** Integración con **MySQL** como motor principal.
* **Operaciones CRUD completas:** Capacidad para crear, leer, actualizar y eliminar registros de `Clientes`, `Cuentas` y `Transacciones`.
* **ORM Avanzado y SQL Raw:** Inclusión de un panel de *Dashboard* que consolida datos usando anotaciones del ORM (`Sum`, `Count`) y sentencias SQL puras mediante `raw()`.
* **Seguridad:** Protección contra ataques CSRF en todos los formularios y restricción de rutas utilizando `LoginRequiredMixin` y el sistema de autenticación preinstalado de Django.

## 🛠️ Tecnologías Utilizadas

* Python 3
* Django 
* MySQL (y `mysqlclient`)
* HTML5 / CSS básico
* Git / GitHub

## ⚙️ Configuración y Ejecución Local

Sigue estos pasos para correr el proyecto en tu máquina local:

1. **Clonar el repositorio:**
   git clone https://github.com/yadielgh-ai/Proyecto-final-modulo-7
   cd proyecto_alke_wallet

2. **Crear y activar el entorno virtual:**
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Mac/Linux:
   source venv/bin/activate

3. **Instalar dependencias:**
   pip install django mysqlclient

4. **Configurar la Base de Datos:**
   * Asegúrate de tener tu servidor MySQL corriendo.
   * Crea una base de datos vacía llamada `alke_wallet_db`.
   * Verifica tus credenciales (usuario y contraseña) en el archivo `alke_wallet/settings.py`.

5. **Aplicar las migraciones:**
   python manage.py migrate

6. **Crear un superusuario (para acceder al admin y a las vistas protegidas):**
   python manage.py createsuperuser

7. **Ejecutar el servidor de desarrollo:**
   python manage.py runserver

   Accede a http://127.0.0.1:8000/clientes/ en tu navegador y loguéate con el superusuario creado.

