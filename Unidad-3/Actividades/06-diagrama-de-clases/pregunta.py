from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado, ayuda, requerida, alternativas_dict):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        
        self.__alternativas = []
        
        for alt in alternativas_dict:
            nueva_alt = Alternativa(alt["contenido"], alt.get("ayuda", ""))
            self.__alternativas.append(nueva_alt)

    @property
    def alternativas(self):
        return self.__alternativas

    def mostrar_pregunta(self):
        if self.ayuda:
            print(f"{self.enunciado} (Ayuda: {self.ayuda})")
        else:
            print(self.enunciado)
            
        for alt in self.__alternativas:
            alt.mostrar_alternativa()