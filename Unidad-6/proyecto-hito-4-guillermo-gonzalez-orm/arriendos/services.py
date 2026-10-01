from .models import TipoInmueble, Inmueble

# Requerimiento 3a: Crear un objeto
def crear_inmueble(nombre, descripcion, direccion, precio, tipo_id):
    """
    Agrega un nuevo inmueble a la base de datos.
    Args:
        nombre (str): Nombre del inmueble.
        descripcion (str): Descripción del inmueble.
        direccion (str): Dirección del inmueble.
        precio (decimal): Precio del inmueble.
        tipo_id (int): ID del TipoInmueble asociado.
    Returns:
        Inmueble: Objeto Inmueble creado o None si hay error.
    """
    try:
        tipo = TipoInmueble.objects.get(id=tipo_id)
        inmueble = Inmueble(
            nombre=nombre,
            descripcion=descripcion,
            direccion=direccion,
            precio=precio,
            tipo_inmueble=tipo
        )
        inmueble.save()
        return inmueble
    except Exception as e:
        print(f"Error al guardar el inmueble: {e}")
        return None

# Requerimiento 3b: Enlistar desde el modelo
def enlistar_inmuebles():
    """Retorna todos los inmuebles registrados en la base de datos."""
    return Inmueble.objects.all()

# Requerimiento 3c: Actualizar un registro
def actualizar_precio_inmueble(inmueble_id, nuevo_precio):
    """Actualiza el precio de un inmueble existente buscando por su ID."""
    try:
        inmueble = Inmueble.objects.get(id=inmueble_id)
        inmueble.precio = nuevo_precio
        inmueble.save()
        return inmueble
    except Exception as e:
        print(f"Error al actualizar el inmueble: {e}")
        return None

# Requerimiento 3d: Borrar un registro
def borrar_inmueble(inmueble_id):
    """Elimina físicamente un registro de inmueble de la base de datos."""
    try:
        inmueble = Inmueble.objects.get(id=inmueble_id)
        inmueble.delete()
        return True
    except Exception as e:
        print(f"Error al borrar el inmueble: {e}")
        return False