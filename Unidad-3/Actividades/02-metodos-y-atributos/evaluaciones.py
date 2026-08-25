from pizza import Pizza

print("--- Atributos de Clase ---")
print(f"Precio de la pizza: ${Pizza.precio}")
print(f"Tamaño de la pizza: {Pizza.tamano}\n")

print("--- Prueba de Validación Estática ---")
elemento_a_validar = "salsa de tomate"
lista_posible = ["salsa de tomate", "salsa bbq"]
es_valido_salsa = Pizza.validar_elemento(elemento_a_validar, lista_posible)
print(f"¿'salsa de tomate' está en la lista?: {es_valido_salsa}\n")

print("--- Nuevo Pedido ---")
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

print("\n--- Detalle del Pedido ---")
print(f"Ingrediente Proteico: {mi_pizza.proteico}")
print(f"Ingredientes Vegetales: {mi_pizza.vegetal_1} y {mi_pizza.vegetal_2}")
print(f"Tipo de Masa: {mi_pizza.masa}")
print(f"¿Es una pizza válida según el menú?: {mi_pizza.es_valida}\n")

print("--- Comprobación de Error Intencional ---")
print(Pizza.es_valida)
