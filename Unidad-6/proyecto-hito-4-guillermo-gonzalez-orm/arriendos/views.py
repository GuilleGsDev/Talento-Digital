from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, InmuebleForm
from .models import Inmueble

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

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tus datos han sido actualizados exitosamente.')
            return redirect('perfil')
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'editar_perfil.html', {'form': form})


# --- NUEVAS VISTAS ORM PARA INMUEBLES ---

# Requerimiento 3.b: Vista para enlistar las viviendas
def listar_inmuebles(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'listar_inmuebles.html', {'inmuebles': inmuebles})

# Requerimiento 1.c: Función para guardar el objeto
@login_required
def nuevo_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inmueble agregado exitosamente.')
            return redirect('listar_inmuebles')
    else:
        form = InmuebleForm()
    return render(request, 'inmueble_form.html', {'form': form, 'accion': 'Agregar'})

# Requerimiento 2.c: Función para actualizar el objeto
@login_required
def editar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inmueble actualizado exitosamente.')
            return redirect('listar_inmuebles')
    else:
        form = InmuebleForm(instance=inmueble)
    return render(request, 'inmueble_form.html', {'form': form, 'inmueble': inmueble, 'accion': 'Actualizar'})

# Requerimiento 2: Borrar inmueble
@login_required
def eliminar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    if request.method == 'POST':
        inmueble.delete()
        messages.success(request, 'Inmueble eliminado exitosamente.')
        return redirect('listar_inmuebles')
    return render(request, 'eliminar_inmueble.html', {'inmueble': inmueble})