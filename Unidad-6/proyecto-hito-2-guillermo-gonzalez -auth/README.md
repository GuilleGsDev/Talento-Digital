# Hito 2 - Implementación de Autenticación de Usuarios

Este proyecto implementa un sistema de autenticación de usuarios para la plataforma de arriendo de inmuebles, utilizando `django-auth`.

## 1. Configuración de la Autenticación
Se verificó la inclusión de `django.contrib.auth` y `django.contrib.contenttypes` en `INSTALLED_APPS` dentro de `settings.py`. Además, se configuraron las variables `LOGIN_REDIRECT_URL` y `LOGOUT_REDIRECT_URL`, y se conectaron las URLs principales del proyecto con las rutas de autenticación por defecto de Django (`django.contrib.auth.urls`). Se utilizó el superusuario creado previamente para administrar el sistema.

*(Opcional: Puedes insertar aquí una captura de tu archivo urls.py o de tu terminal corriendo el servidor)*
![Evidencia Configuración](evidencias/captura_configuracion.png)

## 2. Creación de la Vista y Formulario de Registro
Se creó una vista personalizada en `views.py` utilizando `UserCreationForm` para procesar el registro de nuevos usuarios. Se diseñó un template HTML (`registro.html`) con una interfaz profesional utilizando CSS integrado, permitiendo a los usuarios registrarse correctamente en el sistema.

![Evidencia Formulario de Registro](evidencias/captura_registro.png)

## 3. Vistas de Inicio y Cierre de Sesión
Se implementaron las vistas de inicio y cierre de sesión de Django (`LoginView` y `LogoutView`). Se diseñó el template `login.html` dentro de la carpeta `templates/registration`, manteniendo la línea gráfica profesional del portal. Las vistas permiten ingresar al sistema y cerrar la sesión de forma segura.

![Evidencia Formulario de Login](Evidencias/Captura%20de%20pantalla%202026-09-23%20161638.png)

## 4. Gestión de Permisos y Grupos de Usuarios
A través del panel de administración de Django, se gestionaron los niveles de acceso. Se creó un grupo específico (ej. "Gestores de Arriendo") y se le asignaron permisos granulares relacionados con el modelo `Inmueble` (crear, modificar y ver inmuebles), permitiendo así un control de acceso adecuado para los distintos tipos de usuarios.

![Evidencia Grupos y Permisos](Evidencias/Captura%20de%20pantalla%202026-09-23%20161630.png)