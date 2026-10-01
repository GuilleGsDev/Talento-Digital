from django import forms
from django.contrib.auth.models import User
from .models import Inmueble # Asegúrate de que el modelo se llame Inmueble

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

# Requerimiento 1.b y 2.b: Generar el objeto de formulario en base al modelo
class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = '__all__' # Incluye todos los campos del modelo en el formulario