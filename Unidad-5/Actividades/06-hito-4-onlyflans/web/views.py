from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormForm, ContactFormModelForm
from django.contrib.auth.decorators import login_required

def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def acerca(request):
    return render(request, 'about.html')

@login_required
def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})

def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})

def contacto(request):
    if request.method == 'POST':
        # Reemplazamos ContactFormForm por ContactFormModelForm
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            # Con ModelForm, el guardado directo es así de simple:
            form.save()
            return HttpResponseRedirect('/exito/')
    else:
        # Reemplazamos ContactFormForm por ContactFormModelForm
        form = ContactFormModelForm()
    
    return render(request, 'contactus.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')

def faq(request):
    return render(request, 'faq.html')