from django import forms
from .models import ContactForm

# Tu formulario manual (puedes conservarlo o borrarlo, el desafío no exige borrarlo)
class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')

# NUEVO: El ModelForm automatizado
class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'message']
        labels = {
            'customer_name': 'Nombre',
            'customer_email': 'Correo',
            'message': 'Mensaje',
        }