import preguntas as p
import random

def shuffle_alt(pregunta):
    # Generamos una copia de las alternativas para no romper el diccionario original
    alternativas = pregunta['alternativas'].copy()
    # Mezclamos la lista en su lugar
    random.shuffle(alternativas)
    return alternativas

if __name__ == '__main__':
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1']))