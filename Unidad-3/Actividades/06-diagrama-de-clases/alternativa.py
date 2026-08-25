class Alternativa:
    def __init__(self, contenido, ayuda=""):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar_alternativa(self):
        if self.ayuda:
            print(f"{self.contenido} (Ayuda: {self.ayuda})")
        else:
            print(self.contenido)