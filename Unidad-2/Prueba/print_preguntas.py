import preguntas as p

def print_pregunta(enunciado, alternativas):
    # Imprimir el enunciado (extrayendo el texto de la lista)
    print(enunciado[0], "\n")
    
    # Letras para el formato de la trivia
    letras = ['A', 'B', 'C', 'D']
    for i, alt in enumerate(alternativas):
        print(f"{letras[i]}. {alt[0]}")
        
if __name__ == '__main__':
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])