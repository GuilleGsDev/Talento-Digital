from error import DimensionError

@ancho.setter
def ancho(self, ancho):
    if ancho < 1 or ancho > Foto.MAX:
        raise DimensionError("Error de dimensión en el ancho", ancho, Foto.MAX)
    else:
        self.__ancho = ancho
    
@alto.setter
def alto(self, alto):
    if alto < 1 or alto > Foto.MAX:
        raise DimensionError("Error de dimensión en el alto", alto, Foto.MAX)
    else:
        self.__alto = alto