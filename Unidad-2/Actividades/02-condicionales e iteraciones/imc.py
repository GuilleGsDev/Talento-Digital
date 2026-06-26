peso_persona = float(input("Ingrese su peso en kilogramos: "))
altura_persona = float(input("Ingrese su altura en metros: "))

imc = peso_persona / (altura_persona ** 2)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")
if imc < 18.5:
    print("Usted está en bajo peso.")
elif 18.5 <= imc < 25:
    print("Usted tiene un peso adecuado.")
elif 25 <= imc < 30:
    print("Usted tiene sobrepeso.")
elif 30 <= imc < 35:
    print("Usted tiene obesidad grado I.")
elif 35 <= imc < 40:
    print("Usted tiene obesidad grado II.")
elif imc >= 40:
    print("Usted tiene obesidad grado III.")        