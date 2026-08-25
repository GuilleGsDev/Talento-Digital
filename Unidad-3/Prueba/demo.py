from datetime import date
from campaña import Campaña
from error import Error

datos_anuncios = [
    {
        "tipo": "Video",
        "url_archivo": "http://ejemplo.com/anuncio.mp4",
        "url_clic": "http://ejemplo.com/comprar",
        "sub_tipo": "instream",
        "duracion": 15
    }
]

mi_campana = Campaña(
    nombre="Campaña Lanzamiento",
    fecha_inicio=date.today(),
    fecha_termino=date.today(),
    anuncios=datos_anuncios
)

try:
    print(f"Estado actual de la campaña:\n{mi_campana}\n")
    
    nuevo_nombre = input("Ingrese el nuevo nombre de la campaña:\n")
    nuevo_sub_tipo = input("Ingrese el nuevo sub_tipo para el anuncio de Video:\n")
    
    mi_campana.nombre = nuevo_nombre
    mi_campana.anuncios[0].sub_tipo = nuevo_sub_tipo
    
    print("\n¡Los cambios se han guardado exitosamente!")
    
except Exception as e:
    with open("error.log", "a", encoding="utf-8") as log:
        log.write(f"Excepción capturada: {e}\n")
    
    print("\nHa ocurrido un error en la validación de los datos. Revisa el archivo error.log.")