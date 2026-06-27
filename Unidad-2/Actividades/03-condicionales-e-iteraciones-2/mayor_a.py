import sys
ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

terminal = int(sys.argv[1])  # Obtener el número de terminal desde los argumentos de línea de comandos
ventas_filtradas = {mes: venta for mes, venta in ventas.items() if venta > terminal}

print(ventas_filtradas)
