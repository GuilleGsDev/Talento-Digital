estado_paciente = input("El paciente responde a estimulos? (s/n): ").strip().lower()
if estado_paciente in ("s", "si"):
    print("Valorar la necesidad de trasladar al hospital más cercano")
else:
    print("Abrir via aerea")
    estado_paciente = input("El paciente respira? (s/n): ").strip().lower()
    if estado_paciente in ("s", "si"):
        print("Permitirle posicion de suficiente ventilacion.")
    else:
        print("Administrar 5 ventilaciones y llamar a ambulancia")
        llego_ambulancia = False
        while not llego_ambulancia:
            estado_paciente = input("El paciente tiene signos de vida? (s/n): ").strip().lower()
            if estado_paciente in ("s", "si"):
                print("Reevaluar a la espera de la ambulancia")
            else:
                print("Administrar compresiones torácicas hasta que llegue la ambulancia")
            respuesta_ambulancia = input("¿Ha llegado la ambulancia? (s/n): ").strip().lower()
            if respuesta_ambulancia in ("s", "si"):
                llego_ambulancia = True
                print("La ambulancia ya llegó.")