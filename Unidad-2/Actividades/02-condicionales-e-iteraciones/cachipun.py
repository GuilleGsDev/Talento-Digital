from random import choice

elecciones = ["piedra", "papel", "tijera"]
usuario = input("Elige piedra, papel o tijera: ").lower()
maquina = choice(elecciones)
if usuario not in elecciones:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
elif usuario == maquina:
    print(f"Tu jugaste {usuario}")
    print(f"La computadora jugó {maquina}")
    print(f"Empate!")
elif (usuario == "piedra" and maquina == "tijera") or \
    (usuario == "papel" and maquina == "piedra") or \
    (usuario == "tijera" and maquina == "papel"):
    print(f"Tu jugaste {usuario}")
    print(f"La computadora jugó {maquina}")
    print(f"Ganaste!!")
else:
    print(f"Tu jugaste {usuario}")
    print(f"La computadora jugó {maquina}")
    print(f"Perdiste!")