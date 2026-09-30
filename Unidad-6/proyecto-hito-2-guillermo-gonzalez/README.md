# Configuración del Admin de Django - Hito 2

## 1. Creación de un Superusuario
Para acceder al panel de administración, se generó un superusuario utilizando el comando `python manage.py createsuperuser` en la terminal. Se asignó un nombre de usuario, se omitió el correo (o se ingresó uno válido) y se configuró una contraseña segura.

![Evidencia Creación de Superusuario](Evidencias/Captura%20de%20pantalla%202026-09-23%20153146.png)

## 2. Registro de Modelos en el Admin
Se modificó el archivo `admin.py` de la aplicación para registrar los modelos solicitados (`Inmueble`, `Region` y `Comuna`) utilizando el método `admin.site.register()`.

![Evidencia Registro de Modelos](Evidencias/Captura%20de%20pantalla%202026-09-23%20153346.png)

## 3. Personalización del Panel de Administración
Para mejorar la usabilidad del panel, se crearon clases que heredan de `admin.ModelAdmin` y se vincularon a sus respectivos modelos. Se implementaron las siguientes configuraciones:
* **list_display:** Para mostrar los campos más relevantes en formato de tabla (ej. nombre, precio y dirección en Inmuebles).
* **search_fields:** Para habilitar una barra de búsqueda superior que permite encontrar registros por nombre o descripción.
* **list_filter:** Para habilitar un panel lateral derecho que permite filtrar rápidamente los datos (ej. filtrar inmuebles por precio o comunas por región).

![Evidencia Personalización del Panel](Evidencias/Captura%20de%20pantalla%202026-09-23%20153534.png)