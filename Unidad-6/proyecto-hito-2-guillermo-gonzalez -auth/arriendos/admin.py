from django.contrib import admin
from .models import Inmueble, Region, Comuna

# Personalización del modelo Inmueble
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'precio')
    list_filter = ('precio',) 
    search_fields = ('nombre', 'descripcion')

# Personalización del modelo Region
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

# Personalización del modelo Comuna
class ComunaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'region')
    list_filter = ('region',)
    search_fields = ('nombre',)

# Registro de los modelos vinculados a sus configuraciones
admin.site.register(Inmueble, InmuebleAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Comuna, ComunaAdmin)