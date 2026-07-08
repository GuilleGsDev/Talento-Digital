import preguntas as p

def verificar(alternativas, eleccion):
    # Devuelve el índice de la elección dada reutilizando la variable
    eleccion = ['a', 'b', 'c', 'd'].index(eleccion)
    es_correcta = alternativas[eleccion][1] == 1
    
    if es_correcta:
        print('Respuesta Correcta')
        return True
    else:
        print('Respuesta Incorrecta')
        return False

if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)





