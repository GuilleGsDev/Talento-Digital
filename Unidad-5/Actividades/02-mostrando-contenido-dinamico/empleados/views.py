from django.shortcuts import render

def lista_empleados(request):
    nombres = ['Guillermo González', 'Natalia Ramírez', 'Pedro Pascal', 'Ana Tijoux', 'Claudio Bravo']
    
    contexto = {
        'empleados_empresa': nombres
    }
    
    return render(request, 'empleados.html', contexto)