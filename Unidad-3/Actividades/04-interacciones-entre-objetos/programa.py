from tienda import Restaurante, Supermercado, Farmacia

print("=== Bienvenido al Sistema de Delivery ===")
print("Primero, vamos a crear su tienda.")
print("¿Qué tipo de tienda desea crear?")
print("1. Restaurante")
print("2. Supermercado")
print("3. Farmacia")
tipo_tienda = input("> ")

nombre = input("Ingrese el nombre de la tienda: ")
costo_delivery = int(input("Ingrese el costo de delivery: "))

if tipo_tienda == "1":
    mi_tienda = Restaurante(nombre, costo_delivery)
elif tipo_tienda == "2":
    mi_tienda = Supermercado(nombre, costo_delivery)
else:
    mi_tienda = Farmacia(nombre, costo_delivery)

print(f"\n--- Ingresando productos para {mi_tienda.nombre} ---")
ingresando = True

while ingresando:
    nombre_prod = input("Nombre del producto: ")
    precio_prod = int(input("Precio del producto: "))
    stock_prod = int(input("Stock inicial (0 si es restaurante o no tiene): "))
    
    mi_tienda.ingresar_producto(nombre_prod, precio_prod, stock_prod)
    
    respuesta = input("¿Desea ingresar otro producto? (s/n): ").lower()
    if respuesta == 'n':
        ingresando = False

while True:
    print("\n=== Menú de Opciones ===")
    print("1. Listar productos existentes")
    print("2. Realizar una venta")
    print("3. Salir del programa")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        print("\n" + mi_tienda.listar_productos())
        
    elif opcion == "2":
        nombre_venta = input("Ingrese el nombre del producto que desea vender: ")
        cantidad_venta = int(input("Ingrese la cantidad requerida: "))
        mi_tienda.realizar_venta(nombre_venta, cantidad_venta)
        print("Intento de venta procesado.")
        
    elif opcion == "3":
        print("Cerrando el sistema... ¡Hasta pronto!")
        break 
        
    else:
        print("Opción inválida. Intente nuevamente.")