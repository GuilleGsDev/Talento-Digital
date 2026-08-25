from datetime import date
from error import LargoExcedidoError
from anuncio import Video, Display, Social

class Campaña:

    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: list):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        
        self.__anuncios = []
        
        for ad_dict in anuncios:
            self._crear_anuncio(ad_dict)

    def _crear_anuncio(self, ad_dict: dict):
        tipo = ad_dict.get("tipo")
        if tipo == "Video":
            anuncio = Video(ad_dict["url_archivo"], ad_dict["url_clic"], ad_dict["sub_tipo"], ad_dict["duracion"])
        elif tipo == "Display":
            anuncio = Display(ad_dict["ancho"], ad_dict["alto"], ad_dict["url_archivo"], ad_dict["url_clic"], ad_dict["sub_tipo"])
        elif tipo == "Social":
            anuncio = Social(ad_dict["ancho"], ad_dict["alto"], ad_dict["url_archivo"], ad_dict["url_clic"], ad_dict["sub_tipo"])
        else:
            return 
            
        self.__anuncios.append(anuncio)

    # --- ENCAPSULAMIENTO (GETTERS Y SETTERS) ---
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if len(valor) > 250:
            raise LargoExcedidoError("El nombre de la campaña supera los 250 caracteres permitidos.")
        self.__nombre = valor

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, valor):
        self.__fecha_inicio = valor

    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, valor):
        self.__fecha_termino = valor

    @property
    def anuncios(self):
        return self.__anuncios

    def __str__(self):
        cant_video = sum(1 for ad in self.__anuncios if isinstance(ad, Video))
        cant_display = sum(1 for ad in self.__anuncios if isinstance(ad, Display))
        cant_social = sum(1 for ad in self.__anuncios if isinstance(ad, Social))
        
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {cant_video} Video, {cant_display} Display, {cant_social} Social"