import json
from usuario import Usuario

lista_usuarios = []

with open("usuarios.txt", "r", encoding="utf-8") as archivo_usuarios:
    
    for linea in archivo_usuarios:
        
        try:
            datos_json = json.loads(linea)
            
            nuevo_usuario = Usuario(
                nombre=datos_json["nombre"],
                apellido=datos_json["apellido"],
                email=datos_json["email"],
                genero=datos_json["genero"]
            )
            
            lista_usuarios.append(nuevo_usuario)
            
        except Exception as error_capturado:           
            with open("error.log", "a", encoding="utf-8") as archivo_log:
                # .strip() quita los saltos de línea invisibles para que el log quede ordenado
                archivo_log.write(f"Error al leer linea: {linea.strip()} | Detalle: {error_capturado}\n")

print(f"Proceso finalizado. Se crearon {len(lista_usuarios)} usuarios exitosamente.")
print("Revisa el archivo error.log para ver los registros que fallaron.")