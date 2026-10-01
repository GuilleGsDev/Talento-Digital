import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inmobiliaria.settings') # Asegúrate de que 'inmobiliaria' es el nombre de tu proyecto principal
django.setup()

from arriendos.models import Inmueble, Comuna, Region
from django.db import connection

def exportar_inmuebles_por_comuna():
    # Consulta usando ORM de Django (Requerimiento 2)
    comunas = Comuna.objects.all()
    
    with open('inmuebles_por_comuna.txt', 'w', encoding='utf-8') as archivo:
        archivo.write("--- LISTADO DE INMUEBLES POR COMUNA ---\n\n")
        for comuna in comunas:
            inmuebles = Inmueble.objects.filter(comuna=comuna).values('nombre', 'descripcion')
            if inmuebles.exists():
                archivo.write(f"Comuna: {comuna.nombre}\n")
                for inm in inmuebles:
                    archivo.write(f" - Nombre: {inm['nombre']}\n")
                    archivo.write(f" - Descripción: {inm['descripcion']}\n")
                archivo.write("\n")

def exportar_inmuebles_por_region_sql():
    # Consulta usando SQL puro con cursor (Requerimiento 3)
    query = """
        SELECT r.nombre, i.nombre, i.descripcion 
        FROM arriendos_inmueble i
        JOIN arriendos_comuna c ON i.comuna_id = c.id
        JOIN arriendos_region r ON c.region_id = r.id
        ORDER BY r.nombre;
    """
    
    with open('inmuebles_por_region.txt', 'w', encoding='utf-8') as archivo:
        archivo.write("--- LISTADO DE INMUEBLES POR REGIÓN (SQL) ---\n\n")
        with connection.cursor() as cursor:
            cursor.execute(query)
            resultados = cursor.fetchall()
            
            region_actual = ""
            for fila in resultados:
                region, nombre, descripcion = fila
                if region != region_actual:
                    archivo.write(f"\nRegión: {region}\n")
                    region_actual = region
                
                archivo.write(f" - Nombre: {nombre}\n")
                archivo.write(f" - Descripción: {descripcion}\n")

if __name__ == '__main__':
    print("Ejecutando consultas y generando archivos de texto...")
    exportar_inmuebles_por_comuna()
    exportar_inmuebles_por_region_sql()
    print("¡Listo! Archivos 'inmuebles_por_comuna.txt' y 'inmuebles_por_region.txt' generados exitosamente.")