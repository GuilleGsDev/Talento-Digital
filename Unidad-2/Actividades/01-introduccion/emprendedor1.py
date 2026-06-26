precio_suscripcion = float(input("Ingrese el precio de la suscripción: "))
numero_usuarios = int(input("Ingrese el número de usuarios: "))
gastos_totales = float(input("Ingrese los gastos totales: "))

utilidades = (precio_suscripcion * numero_usuarios) - gastos_totales
print(f"Las utilidades son: {utilidades}")