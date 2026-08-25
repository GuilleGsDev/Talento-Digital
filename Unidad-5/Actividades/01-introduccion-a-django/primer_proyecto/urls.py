from django.contrib import admin
from django.urls import path
# Importamos las 3 vistas que acabamos de crear en tu proyecto
from primer_proyecto.views import home, about, contact 

# Conectamos las rutas de la web con las funciones de las vistas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),           # Ruta vacía para el Home
    path('about/', about),    # Ruta para la página About
    path('contact/', contact) # Ruta para la página Contact
]