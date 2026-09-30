from django.contrib import admin
from django.urls import path, include
from arriendos.views import registro 

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluye las rutas por defecto de Django para login/logout
    path('accounts/', include('django.contrib.auth.urls')), 
    # Ruta para nuestra vista de registro
    path('registro/', registro, name='registro'),
]