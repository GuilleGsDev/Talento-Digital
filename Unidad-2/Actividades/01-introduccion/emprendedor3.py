precio_suscripcion = float(input("Ingrese el precio de la suscripción: "))
numero_usuarios = int(input("Ingrese el número de usuarios: "))
gastos_totales = float(input("Ingrese los gastos totales: "))
utilidades_anterior = float(input("Ingrese las utilidades del año anterior: "))

utilidades = (precio_suscripcion * numero_usuarios) - gastos_totales
razon_utilidades = utilidades / utilidades_anterior

print(f"La razón entre las utilidades es: {razon_utilidades:.2f}")