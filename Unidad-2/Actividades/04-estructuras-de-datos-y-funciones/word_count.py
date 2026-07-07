with open("lorem_ipsum.txt", "r") as file:
    text = file.read()
caracteres_distintos = set(text)
total_caracteres_distintos = len(caracteres_distintos)
lista_palabras = text.split()
palabras_distintas = set(lista_palabras)
total_palabras_distintas = len(palabras_distintas)
print("El número de caracteres distintos es:", total_caracteres_distintos)
print("El número de palabras distintas es:", total_palabras_distintas)