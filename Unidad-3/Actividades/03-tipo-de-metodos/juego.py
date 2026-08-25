import random 
from personaje import Personaje

print("Bienvenido a Gran Fantasia")
nombre_jugador = input("Ingresa tu nombre: ")

jugador = Personaje(nombre_jugador)
print(jugador.estado)

print("\n¡Oh no!, ¡Ha aparecido un Orco!")
orco = Personaje("Orco")

probabilidad = jugador.get_probabilidad(orco)
opcion = Personaje.mostrar_dialogo_opcion(probabilidad)

while opcion == 1:
    resultado_azar = random.uniform(0, 1)    
    if resultado_azar <= probabilidad:
        print("\n¡Le has ganado al orco, felicidades!")
        print("¡Recibirás 50 puntos de experiencia!")
        jugador.estado = 50
        orco.estado = -30
    else:
        print("\n¡Oh no! ¡El orco te ha ganado!")
        print("¡Has perdido 30 puntos de experiencia!")
        jugador.estado = -30
        orco.estado = 50        
    print(jugador.estado)
    print(orco.estado)
    probabilidad = jugador.get_probabilidad(orco)
    opcion = Personaje.mostrar_dialogo_opcion(probabilidad)
print("\n¡Has huido! El orco ha quedado atrás.")