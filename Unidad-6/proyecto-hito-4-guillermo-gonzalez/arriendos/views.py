from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm

def home(request):
    return render(request, 'home.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso! Bienvenido.')
            return redirect('perfil')
    else:
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'perfil.html', {'user': request.user})

# Requerimiento 2: Vista para modificar datos personales
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        # Pasamos instance=request.user para que actualice al usuario logueado actual
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tus datos han sido actualizados exitosamente.')
            return redirect('perfil')
    else:
        # Si es GET, pre-cargamos el formulario con los datos actuales del usuario
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'editar_perfil.html', {'form': form})