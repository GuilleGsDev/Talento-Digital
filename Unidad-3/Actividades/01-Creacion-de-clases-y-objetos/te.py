class Te():
    duracion = 365 

    @staticmethod
    def tiempo_y_recomendacion(sabor: int):
        if sabor == 1:
            return 3, "Se recomienda tomarlo al desayuno"
        elif sabor == 2:
            return 5, "Se recomienda tomarlo al media día"
        elif sabor == 3:
            return 6, "Se recomienda tomarlo al atardecer"
    
    @staticmethod
    def obtener_precio(formato: int):
        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000