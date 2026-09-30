# Proyecto Inmobiliaria - Hito 1

## Configuración del Entorno
- Se creó la base de datos `arriendos_db` en PostgreSQL.
- Se configuró un entorno virtual con Python.
- Se instalaron las librerías `django` y `psycopg2` (registradas en requirements.txt).
- Se inicializó el proyecto `inmobiliaria` y la aplicación `arriendos`.

## Modelos de Datos (Requerimiento 2)
- Se conectó el proyecto a `arriendos_db` en PostgreSQL.
- Se crearon los modelos `TipoInmueble` e `Inmueble`.
- Se implementó una llave foránea (Foreign Key) en `Inmueble` que se relaciona con `TipoInmueble`.

## Operaciones CRUD (Requerimiento 3)
Se creó el archivo `services.py` dentro de la aplicación `arriendos` para manejar la lógica de datos. Se implementaron las siguientes funciones utilizando buenas prácticas (Manejo de errores try/except y Docstrings):
- **Crear:** Función `crear_inmueble` para instanciar y guardar registros.
- **Enlistar:** Función `enlistar_inmuebles` para obtener todos los registros con `.all()`.
- **Actualizar:** Función `actualizar_precio_inmueble` para modificar el precio de un inmueble.
- **Borrar:** Función `borrar_inmueble` utilizando el método `.delete()` de Django.