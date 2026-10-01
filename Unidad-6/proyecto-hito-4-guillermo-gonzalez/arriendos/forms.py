from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        # Definimos los campos que el usuario podrá modificar en su perfil
        fields = ['first_name', 'last_name', 'email']