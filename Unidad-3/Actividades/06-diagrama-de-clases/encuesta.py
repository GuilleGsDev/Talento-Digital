from pregunta import Pregunta

class Encuesta:
    def __init__(self, nombre, preguntas_dict):
        self.nombre = nombre
        self.__listados_respuestas = [] 
        
        self.__preguntas = []
        for p in preguntas_dict:
            nueva_pregunta = Pregunta(
                p["enunciado"],
                p.get("ayuda", ""),
                p["requerida"],
                p["alternativas"]
            )
            self.__preguntas.append(nueva_pregunta)

    def mostrar_encuesta(self):
        print(f"=== Encuesta: {self.nombre} ===")
        for p in self.__preguntas:
            p.mostrar_pregunta()
            print("") 

    def agregar_listado_respuestas(self, listado_respuestas):
        self.__listados_respuestas.append(listado_respuestas)

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre, preguntas_dict, edad_min, edad_max):
        super().__init__(nombre, preguntas_dict)
        self.__edad_min = edad_min
        self.__edad_max = edad_max

    def agregar_listado_respuestas(self, listado_respuestas):
        if self.__edad_min <= listado_respuestas.usuario.edad <= self.__edad_max:
            super().agregar_listado_respuestas(listado_respuestas)


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, preguntas_dict, regiones):
        super().__init__(nombre, preguntas_dict)
        self.__regiones = regiones

    def agregar_listado_respuestas(self, listado_respuestas):
        if listado_respuestas.usuario.region in self.__regiones:
            super().agregar_listado_respuestas(listado_respuestas)