class Personaje():
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    @property
    def estado(self):
        return f"NOMBRE: {self.nombre}\nNIVEL: {self.nivel}\nEXP: {self.experiencia}"
    
    @estado.setter
    def estado(self, exp_recibida):
        temp_exp = self.experiencia + exp_recibida
        while temp_exp >= 100:
            self.nivel += 1
            temp_exp -= 100
        while temp_exp < 0:
            if self.nivel > 1:
                self.nivel -= 1
                temp_exp += 100
            else:
                temp_exp = 0
        self.experiencia = temp_exp

    def __lt__(self, otro):
        return self.nivel < otro.nivel

    def __gt__(self, otro):
        return self.nivel > otro.nivel

    def __eq__(self, otro):
        return self.nivel == otro.nivel

    def get_probabilidad(self, otro):
        if self < otro:
            return 0.33
        elif self > otro:
            return 0.66
        else:
            return 0.50

    @staticmethod
    def mostrar_dialogo_opcion(probabilidad):
        print(f"\nCon tu nivel actual, tienes {probabilidad * 100}% de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        print("¿Qué deseas hacer?")
        print("1. Atacar")
        print("2. Huir")
        opcion = int(input("> "))
        return opcion