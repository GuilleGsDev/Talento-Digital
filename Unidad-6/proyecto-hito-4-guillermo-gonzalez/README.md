# Hito 4 - Creando una aplicación usando datos con Django y el patrón MVC

Este proyecto implementa la capa de acceso a datos en un aplicativo web utilizando el patrón MVC para la plataforma de arriendo de inmuebles, integrando la autenticación de usuarios y la gestión de sus perfiles personales.

## 1. Vistas de Autenticación y Perfil
Se crearon las vistas y plantillas necesarias para la interacción de los usuarios (Arrendatarios y Arrendadores) con el sistema:
- **Registro y Login:** Se implementó una vista de registro utilizando `UserCreationForm` que loguea automáticamente al usuario al finalizar, junto con la vista de inicio de sesión genérica de Django.
- **Redireccionamiento:** Se configuraron las rutas en `urls.py` y los parámetros `LOGIN_REDIRECT_URL` y `LOGOUT_REDIRECT_URL` en `settings.py` para asegurar un flujo de navegación correcto.
- **Despliegue de Datos:** Se creó una página personal (`perfil.html`) que despliega la información del usuario autenticado (nombre de usuario, nombre, apellido y correo), todo bajo un template básico (`base.html`) estructurado con un diseño profesional y colores corporativos.

## 2. Modificación de Datos Personales
Se agregó la funcionalidad para que los usuarios puedan actualizar su información personal directamente desde su perfil:
- **Formulario de Actualización:** Se creó el formulario `UserUpdateForm` para permitir la modificación segura de los datos (nombre, apellido y correo electrónico).
- **Vista de Edición (CRUD):** Se implementó la vista `editar_perfil`, protegida para que solo usuarios logueados puedan acceder, encargada de procesar y guardar los cambios en la base de datos.
- **Feedback al Usuario:** Se integró el sistema de mensajes de Django para notificar de forma visual cuando los datos personales se actualizan exitosamente.