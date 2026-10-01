from django.db import models

class TipoInmueble(models.Model):
    """Modelo que representa las categorías de los inmuebles (ej. Casa, Departamento)."""
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Inmueble(models.Model):
    """Modelo que representa una vivienda disponible para el arriendo."""
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE, related_name='inmuebles')
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE, related_name='inmuebles', null=True)
    
    def __str__(self):
        return self.nombre

class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='comunas')

    def __str__(self):
        return self.nombre