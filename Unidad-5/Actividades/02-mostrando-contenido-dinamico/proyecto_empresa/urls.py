from django.contrib import admin
from django.urls import path
from empleados.views import lista_empleados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_empleados), # La ruta vacía cargará tu lista de empleados
]