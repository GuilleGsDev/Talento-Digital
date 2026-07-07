sol_peruano = 0.0046
peso_argentino = 0.093
dolar_americano = 0.0013
peso_chileno = float(input("Ingrese la cantidad de pesos chilenos: "))
print(f"Los {peso_chileno} pesos equivalen a:")
print(f"{peso_chileno * sol_peruano:.1f} soles")
print(f"{peso_chileno * peso_argentino:.1f} pesos argentinos")
print(f"{peso_chileno * dolar_americano:.1f} dólares")