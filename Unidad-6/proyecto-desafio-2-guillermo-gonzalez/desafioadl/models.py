from django.db import models

class Tarea(models.Model):
    # Django crea el campo 'id' automáticamente como Primary Key y autoincremental, 
    # pero lo definimos explícitamente para seguir el diagrama al pie de la letra.
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(default="")
    eliminada = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion

class SubTarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(default="")
    eliminada = models.BooleanField(default=False)
    # FK1: Relación hacia el modelo Tarea
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='subtareas')

    def __str__(self):
        return self.descripcion