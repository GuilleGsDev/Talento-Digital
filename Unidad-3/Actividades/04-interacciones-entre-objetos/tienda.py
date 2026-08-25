from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def costo_delivery(self):
        return self.__costo_delivery

    @property
    def productos(self):
        return self.__productos

    def ingresar_producto(self, nombre, precio, stock):
        for p in self.__productos:
            if p.nombre == nombre:
                p.stock += stock
                return 

        nuevo_producto = Producto(nombre, precio, stock)
        self.__productos.append(nuevo_producto)

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass

class Restaurante(Tienda):
    def ingresar_producto(self, nombre, precio, stock):
        super().ingresar_producto(nombre, precio, 0)

    def listar_productos(self):
        resultado = f"--- Menú de {self.nombre} ---\n"
        for p in self.productos:
            resultado += f"Producto: {p.nombre} | Precio: ${p.precio}\n"
        return resultado

        def realizar_venta(self, nombre_producto, cantidad):
            pass

class Supermercado(Tienda):
    
    def listar_productos(self):
        resultado = f"--- Pasillos de {self.nombre} ---\n"
        for p in self.productos:
            texto_stock = f"Stock: {p.stock}"
            if p.stock < 10:
                texto_stock += " - Pocos productos disponibles"
                
            resultado += f"Producto: {p.nombre} | Precio: ${p.precio} | {texto_stock}\n"
        return resultado

    def realizar_venta(self, nombre_producto, cantidad):
        for p in self.productos:
            if p.nombre == nombre_producto:
                if cantidad > p.stock:
                    p.stock = 0
                else:
                    p.stock -= cantidad
                return 
            
class Farmacia(Tienda):
    
    def listar_productos(self):
        resultado = f"--- Estantes de {self.nombre} ---\n"
        for p in self.productos:
            texto_precio = f"${p.precio}"
            if p.precio > 15000:
                texto_precio += " - Envío gratis al solicitar este producto"
                
            resultado += f"Producto: {p.nombre} | Precio: {texto_precio}\n"
        return resultado

    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad > 3:
            return 
            
        for p in self.productos:
            if p.nombre == nombre_producto:
                if cantidad > p.stock:
                    p.stock = 0
                else:
                    p.stock -= cantidad
                return