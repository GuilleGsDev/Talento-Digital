from math import sqrt

radio = float(input("Ingrese el radio en Kilometros: "))
constante = float(input("Ingrese la constante de gravedad: "))

radio = radio * 1000  # Convertir a metros
velocidad_escape = sqrt(2 * constante * radio)

print(f"La velocidad de escape es: {velocidad_escape:.1f} [m/s]")