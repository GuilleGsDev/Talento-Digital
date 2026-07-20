from te import Te

print("--- Selección de Té ---")
print("1: Té negro | 2: Té verde | 3: Agua de hierbas")
sabor_ingresado = int(input("Ingrese el número correspondiente al sabor: "))

print("\n--- Formato ---")
formato_ingresado = int(input("Ingrese el formato en gramos (300 o 500): "))

tiempo, recomendacion = Te.tiempo_y_recomendacion(sabor_ingresado)
precio = Te.obtener_precio(formato_ingresado)

sabor_texto = ""
if sabor_ingresado == 1:
    sabor_texto = "Té negro"
elif sabor_ingresado == 2:
    sabor_texto = "Té verde"
elif sabor_ingresado == 3:
    sabor_texto = "Agua de hierbas"

print("\n=================================")
print("      DETALLE DEL PEDIDO         ")
print("=================================")
print(f"Sabor del té:    {sabor_texto}")
print(f"Formato:         {formato_ingresado} gr")
print(f"Precio:          ${precio}")
print(f"Tiempo prepar.:  {tiempo} minutos")
print(f"Recomendación:   {recomendacion}")
print("=================================")