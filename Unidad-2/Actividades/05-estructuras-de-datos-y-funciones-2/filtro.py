import sys

precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

def filtrar_productos():
    #Validar que se ingrese al menos el umbral
    if len(sys.argv) < 2:
        print("Por favor, ingrese un umbral numerico.")
        return
    
    # Capturar el umbral y convertirlo a número entero
    try:
        umbral = int(sys.argv[1])
    except ValueError:
        print("Por favor, ingrese un umbral numerico.")
        return
    
    # Definir la operación por defecto
    operacion = 'mayor'
    if len(sys.argv) == 3:
        operacion = sys.argv[2].lower()

    # Validar que la operación sea correcta ('mayor' o 'menor')
    if operacion not in ["mayor", "menor"]:
        print("Lo sentimos, no es una operación válida")
        return
    
    # Filtrar según la operación solicitada
    if operacion == "mayor":
        filtrados = [producto for producto, precio in precios.items() if precio > umbral]
        print(f"Los productos mayores al umbral son: {', '.join(filtrados)}")
    else:
        filtrados = [producto for producto, precio in precios.items() if precio < umbral]
        print(f"Los productos menores al umbral son: {', '.join(filtrados)}")

if __name__ == "__main__":
    filtrar_productos()