class Pizza :
    precio = 10000
    tamano = "familiar"
    ingredientes_proteicos = ["pollo", "vacuno", "carne vegetal"]
    ingredientes_vegetales = ["tomate", "aceitunas", "champiñones"]
    masa_posible = ["tradicional", "delgada" ]

    @staticmethod
    def validar_elemento (elemento: str, posible_elementos: list) -> bool:
        return elemento in posible_elementos
    
    def realizar_pedido (self):
        self.proteico = input("Ingrese el ingrediente proteico (pollo, vacuno, carne vegetal): ")
        self.vegetal_1 = input("Ingrese el 1er ingrediente vegetal (tomate, aceitunas, champiñones): ")
        self.vegetal_2 = input("Ingrese el 2do ingrediente vegetal (tomate, aceitunas, champiñones): ")
        self.masa = input("Ingrese el tipo de masa (tradicional, delgada): ")
        
        valido_prot = self.validar_elemento(self.proteico, self.ingredientes_proteicos)
        valido_veg1 = self.validar_elemento(self.vegetal_1, self.ingredientes_vegetales)
        valido_veg2 = self.validar_elemento(self.vegetal_2, self.ingredientes_vegetales)
        valido_masa = self.validar_elemento(self.masa, self.masa_posible)

        if valido_prot and valido_veg1 and valido_veg2 and valido_masa:
            self.es_valido = True
        else:
            self.es_valido = False
