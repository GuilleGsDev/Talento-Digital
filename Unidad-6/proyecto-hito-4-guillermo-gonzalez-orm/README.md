# Hito 4 - Creando una aplicación usando datos con Django y su ORM

Este proyecto implementa operaciones CRUD (Crear, Leer, Actualizar, Borrar) utilizando el ORM de Django para la gestión de inmuebles dentro de la plataforma de arriendos.

## 1. Gestión de Inmuebles (CRUD)
Se desarrollaron las vistas, rutas y formularios necesarios para que los usuarios (arrendadores) puedan administrar la oferta de viviendas:
- **Listar Oferta (Read):** Vista pública (`listar_inmuebles`) que consulta y despliega todos los inmuebles registrados en la base de datos utilizando el ORM de Django.
- **Agregar Inmueble (Create):** Implementación de `InmuebleForm` y la vista `nuevo_inmueble` para registrar nuevas propiedades, protegida para usuarios autenticados.
- **Actualizar Inmueble (Update):** Vista `editar_inmueble` que recupera la instancia específica del inmueble mediante `get_object_or_404` y permite modificar sus atributos.
- **Eliminar Inmueble (Delete):** Vista `eliminar_inmueble` que solicita confirmación antes de borrar permanentemente el registro de la base de datos.

## 2. Interfaz y Experiencia de Usuario
- **Navegación:** Se integró un enlace directo en la barra de navegación principal para acceder al listado de propiedades.
- **Control de Acceso:** Los botones de edición y eliminación se renderizan condicionalmente solo si el usuario está autenticado (`user.is_authenticated`), y las vistas están protegidas con el decorador `@login_required`.
- **Feedback Visual:** Uso del sistema de mensajes de Django para confirmar el éxito de cada operación CRUD ejecutada por el usuario.