precio_suscripcion = float(input("Ingrese el precio de la suscripción: "))
usuarios_normales = int(input("Ingrese el número de usuarios normales: "))
usuarios_premium = int(input("Ingrese el número de usuarios premium: "))
gastos_totales = float(input("Ingrese los gastos totales: "))

ingresos_premium = (precio_suscripcion * 1.5) * usuarios_premium  # Los usuarios premium pagan un 50% más
ingresos_normales = (precio_suscripcion * usuarios_normales)

utilidades = ingresos_normales + ingresos_premium - gastos_totales
print(f"Las utilidades son: {utilidades}")