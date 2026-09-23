from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    # Retorna todas las tareas cuyo campo 'eliminada' sea False
    return Tarea.objects.filter(eliminada=False)

def crear_nueva_tarea(descripcion):
    # Crea la tarea, la guarda y retorna el arreglo actualizado
    tarea = Tarea(descripcion=descripcion)
    tarea.save()
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id, descripcion):
    # Busca la tarea padre, crea la subtarea asociada y retorna el arreglo
    tarea = Tarea.objects.get(id=tarea_id)
    subtarea = SubTarea(tarea=tarea, descripcion=descripcion)
    subtarea.save()
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    # Borrado lógico: cambia el estado a eliminada=True
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.eliminada = True
    tarea.save()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(subtarea_id):
    # Borrado lógico de la subtarea
    subtarea = SubTarea.objects.get(id=subtarea_id)
    subtarea.eliminada = True
    subtarea.save()
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(arreglo):
    # Recibe el arreglo e imprime con el formato solicitado en el documento
    for tarea in arreglo:
        print(f"[{tarea.id}] {tarea.descripcion}")
        # Accedemos a las subtareas asociadas usando el related_name 'subtareas'
        # y filtramos para no mostrar las que estén eliminadas lógicamente
        for subtarea in tarea.subtareas.filter(eliminada=False):
            print(f".... [{subtarea.id}] {subtarea.descripcion}")