# Función para calcular el factorial de un número
def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Función para calcular la productoria de una lista
def calcular_productoria(lista):
    productoria = 1
    for elemento in lista:
        productoria *= elemento
    return productoria

# Función controladora que recibe argumentos variables con nombre
def calcular(**kwargs):
    for clave, valor in kwargs.items():
        if 'fact' in clave:
            resultado = calcular_factorial(valor)
            print(f"El factorial de {valor} es {resultado}")
        elif 'prod' in clave:
            resultado = calcular_productoria(valor)
            print(f"La productoria de {valor} es {resultado}")

if __name__ == "__main__":
    # Prueba solicitada en el enunciado
    calcular(fact_1 = 5, prod_1 = [3, 6, 4, 2, 8], fact_2 = 6)