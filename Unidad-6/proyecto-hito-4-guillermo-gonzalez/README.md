# Hito 3 - Migraciones y Recuperación de Datos con Django

Este proyecto implementa la configuración de base de datos, carga de datos iniciales (fixtures) y consultas mediante ORM y SQL puro para la plataforma de arriendo de inmuebles.

## 1. Migraciones y Población de Base de Datos
Se utilizó la herramienta de migraciones de Django para estructurar la base de datos y conectar correctamente los modelos `Inmueble`, `TipoInmueble`, `Region` y `Comuna`. 
Posteriormente, se utilizó el comando `loaddata` para poblar la base de datos a partir de archivos JSON (`fixtures`), cumpliendo con la carga de:
- Regiones y Comunas.
- Tipos de Inmuebles.
- Usuarios de prueba e Inmuebles asociados a las comunas.

![Evidencia de carga de datos loaddata](Evidencias/Captura%20de%20pantalla%202026-09-28%20111646.png)

## 2. Consultas y Reportes (ORM y SQL)
Se creó un script de Python (`consultas.py`) configurado para interactuar con el entorno de Django y la base de datos, el cual automatiza la generación de dos reportes en formato texto:
- **Reporte por Comunas (ORM):** Utiliza el ORM de Django para filtrar y listar los inmuebles disponibles separados por comuna, extrayendo únicamente los campos `nombre` y `descripción`.
- **Reporte por Regiones (SQL Puro):** Utiliza un cursor de conexión (`connection.cursor()`) para ejecutar una sentencia `JOIN` en SQL puro, cruzando las tablas de Inmuebles, Comunas y Regiones para estructurar los resultados.

![Evidencia ejecución del script](Evidencias/Captura%20de%20pantalla%202026-09-28%20112555.png)
*(Se adjuntan los archivos `inmuebles_por_comuna.txt` y `inmuebles_por_region.txt` generados por el script en la raíz del proyecto).*