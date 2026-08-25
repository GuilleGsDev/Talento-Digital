from listado_respuestas import ListadoRespuestas

class Usuario:
    def __init__(self, correo, edad, region):
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    @property
    def correo(self):
        return self.__correo

    @property
    def edad(self):
        return self.__edad

    @property
    def region(self):
        return self.__region

    def contestar_encuesta(self, encuesta, respuestas):
        nuevo_listado = ListadoRespuestas(self, respuestas)
        encuesta.agregar_listado_respuestas(nuevo_listado)