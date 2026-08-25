class ListadoRespuestas:
    def __init__(self, usuario, respuestas):
        # Ambos atributos son privados según el requerimiento
        self.__usuario = usuario
        self.__respuestas = respuestas

    # Getters para poder consultar la información sin modificarla
    @property
    def usuario(self):
        return self.__usuario

    @property
    def respuestas(self):
        return self.__respuestas