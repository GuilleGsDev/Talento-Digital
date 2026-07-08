pizza = {
    "masa": "Masa Tradicional",
    "salsa": "Salsa de Tomate",
    "ingredientes": ["Queso"]  # Comienza con un ingrediente base
}

# Listas de opciones disponibles
MASAS_DISPONIBLES = ["Masa Tradicional", "Masa Delgada", "Masa con Bordes de Queso"]
SALSAS_DISPONIBLES = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]
INGREDIENTES_DISPONIBLES = ["Tomate", "Champiñones", "Aceituna", "Cebolla", "Pollo", "Jamón", "Carne", "Tocino", "Queso"]

def mostrar_ingredientes():
    """Muestra la configuración actual de la pizza (Requerimiento 3)."""
    print("\n--- RESUMEN DE TU PIZZA ---")
    print(f"-> Masa: {pizza['masa']}")
    print(f"-> Salsa: {pizza['salsa']}")
    print(f"-> Ingredientes actuales: {', '.join(pizza['ingredientes']) if pizza['ingredientes'] else 'Ninguno'}")
    print("---------------------------\n")

def cambiar_masa():
    """Permite al usuario cambiar el tipo de masa (Requerimiento 1.a)."""
    print("\nSelecciona el tipo de masa:")
    for i, masa in enumerate(MASAS_DISFINIBLES := MASAS_DISPONIBLES, 1):
        print(f"{i}. {masa}")
    
    try:
        opcion = int(input("Ingrese el número de su opción: "))
        if 1 <= opcion <= len(MASAS_DISPONIBLES):
            pizza["masa"] = MASAS_DISPONIBLES[opcion - 1]
            print(f"¡Masa cambiada exitosamente a: {pizza['masa']}!")
        else:
            print("Opción inválida. No se realizaron cambios.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")

def cambiar_salsa():
    """Permite al usuario cambiar el tipo de salsa (Requerimiento 1.b)."""
    print("\nSelecciona el tipo de salsa:")
    for i, salsa in enumerate(SALSAS_DISPONIBLES, 1):
        print(f"{i}. {salsa}")
    
    try:
        opcion = int(input("Ingrese el número de su opción: "))
        if 1 <= opcion <= len(SALSAS_DISPONIBLES):
            pizza["salsa"] = SALSAS_DISPONIBLES[opcion - 1]
            print(f"¡Salsa cambiada exitosamente a: {pizza['salsa']}!")
        else:
            print("Opción inválida. No se realizaron cambios.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")

def modificar_ingredientes():
    """Permite agregar o eliminar ingredientes de la pizza (Requerimiento 1.c)."""
    print("\n¿Qué desea hacer con los ingredientes?")
    print("1. Agregar un ingrediente")
    print("2. Eliminar un ingrediente")
    accion = input("Seleccione 1 o 2: ")

    if accion == "1":
        print("\nIngredientes disponibles para agregar:")
        # Mostrar solo los ingredientes que NO están ya en la pizza
        disponibles = [ing for ing in INGREDIENTES_DISPONIBLES if ing not in pizza["ingredientes"]]
        if not disponibles:
            print("¡Ya tienes todos los ingredientes posibles en tu pizza!")
            return
        
        for i, ing in enumerate(disponibles, 1):
            print(f"{i}. {ing}")
        
        try:
            opcion = int(input("Seleccione el ingrediente a agregar: "))
            if 1 <= opcion <= len(disponibles):
                pizza["ingredientes"].append(disponibles[opcion - 1])
                print(f"¡Se agregó {disponibles[opcion - 1]} a tu pizza!")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Debe ingresar un número.")

    elif accion == "2":
        if not pizza["ingredientes"]:
            print("Tu pizza no tiene ingredientes para eliminar.")
            return
        
        print("\nIngredientes actuales en tu pizza:")
        for i, ing in enumerate(pizza["ingredientes"], 1):
            print(f"{i}. {ing}")
        
        try:
            opcion = int(input("Seleccione el número del ingrediente a eliminar: "))
            if 1 <= opcion <= len(pizza["ingredientes"]):
                eliminado = pizza["ingredientes"].pop(opcion - 1)
                print(f"¡Se eliminó {eliminado} de tu pizza!")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Debe ingresar un número.")
    else:
        print("Opción no válida.")

def confirmar_orden():
    """Calcula el tiempo estimado y procesa la confirmación del pedido (Requerimiento 2)."""
    # Fórmula: 20 minutos base + 2 minutos por cada ingrediente (excluyendo masa y salsa)
    tiempo_estimado = 20 + (2 * len(pizza["ingredientes"]))
    
    mostrar_ingredientes()
    print(f"El tiempo estimado de preparación es de {tiempo_estimado} minutos.")
    confirmar = input("¿Desea confirmar su orden? (si/no): ").strip().lower()
    
    if confirmar == "si":
        print("\n¡Tu orden ha sido procesada! Gracias por elegir Pizza JAT. ¡Disfruta!")
        return True
    else:
        print("\nPedido cancelado o guardado. Puedes seguir personalizándolo.")
        return False

def menu_interactivo():
    """Controla el flujo principal de la aplicación de consola."""
    while True:
        print("\n========== BIENVENIDO A PIZZA JAT ==========")
        print("1. Cambiar tipo de masa")
        print("2. Cambiar tipo de salsa")
        print("3. Modificar ingredientes (Agregar/Eliminar)")
        print("4. Mostrar ingredientes actuales")
        print("5. Calcular tiempo y Confirmar Pedido")
        print("6. Salir de la aplicación")
        print("=============================================")
        
        opcion = input("Por favor, seleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            cambiar_masa()
        elif opcion == "2":
            cambiar_salsa()
        elif opcion == "3":
            modificar_ingredientes()
        elif opcion == "4":
            mostrar_ingredientes()
        elif opcion == "5":
            # Si el pedido se confirma exitosamente, terminamos el programa
            if confirmar_orden():
                break
        elif opcion == "6":
            print("Gracias por visitar Pizza JAT. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo del 1 al 6.")

# Ejecución del programa
if __name__ == "__main__":
    menu_interactivo()