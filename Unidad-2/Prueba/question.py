import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones disponibles por nivel (1, 2 y 3)
opciones = {'basicas': [1, 2, 3],
            'intermedias': [1, 2, 3],
            'avanzadas': [1, 2, 3]}

def choose_q(dificultad):
    global opciones
    
    # 1. Tomar las preguntas disponibles de la dificultad elegida
    preguntas_disponibles = opciones[dificultad]
    
    # 2. Escoger una al azar
    n_elegido = random.choice(preguntas_disponibles)
    
    # 3. Eliminarla del ambiente global para no repetirla
    opciones[dificultad].remove(n_elegido)
    
    # 4. Obtener la pregunta del pool_preguntas usando la clave correspondiente
    clave_pregunta = f'pregunta_{n_elegido}'
    pregunta = p.pool_preguntas[dificultad][clave_pregunta]
    
    # 5. Mezclar sus alternativas
    alternativas = shuffle_alt(pregunta)
    
    # Retornamos el enunciado y las alternativas mezcladas
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')