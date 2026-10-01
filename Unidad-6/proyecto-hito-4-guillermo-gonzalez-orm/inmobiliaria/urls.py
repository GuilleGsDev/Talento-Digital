from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from arriendos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    
    # Requerimiento 3.a: Rutas para ver las viviendas
    path('inmuebles/', views.listar_inmuebles, name='listar_inmuebles'),
    
    # Requerimiento 1.a: Ruta para agregar nuevas viviendas
    path('inmuebles/nuevo/', views.nuevo_inmueble, name='nuevo_inmueble'),
    
    # Requerimiento 2.a: Rutas para actualizar/borrar viviendas
    path('inmuebles/editar/<int:id>/', views.editar_inmueble, name='editar_inmueble'),
    path('inmuebles/eliminar/<int:id>/', views.eliminar_inmueble, name='eliminar_inmueble'),
]