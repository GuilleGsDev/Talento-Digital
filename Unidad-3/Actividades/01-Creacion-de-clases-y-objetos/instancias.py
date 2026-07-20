from te import Te

te_1 = Te()
te_2 = Te()

tipo_1 = type(te_1)
tipo_2 = type(te_2)

print(f"Tipo del objeto 1: {tipo_1}")
print(f"Tipo del objeto 2: {tipo_2}")

if tipo_1 == tipo_2:
    print("Los objetos son del mismo tipo.")
else:
    print("Los objetos son de tipos diferentes.")    