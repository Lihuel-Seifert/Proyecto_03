from django.shortcuts import render
from Aplicaciones.models import *
from Aplicaciones.forms import *
# Create your views here.

def cursos(request):

    datos = Cursos.objects.all()

    # Buscador <----
    if request.GET.get("buscar"):
        
        formulario = Busqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            datos = Cursos.objects.filter(codigo__icontains = data["buscar"])
        
        return render(request,'Aplicaciones/index2.html', {'datos':datos, "formulario" : formulario})

    else:
        formulario = Busqueda()
        return render(request,'Aplicaciones/index2.html', {'datos':datos, "formulario" : formulario})

def notas(request):
    
    datos1 = Notas.objects.all()

    # Buscador <----
    if request.GET.get("buscar"):
        
        formulario = Busqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            datos1 = Notas.objects.filter(codigo__icontains = data["buscar"])
        
        return render(request,'Aplicaciones/notas.html', {'datos1':datos1, "formulario" : formulario})
        
    else:
        formulario = Busqueda()
        return render(request,'Aplicaciones/notas.html', {'datos1':datos1, "formulario" : formulario})

def alumnos(request):
    
    datos2= Alumnos.objects.all()

    # Buscador <----
    if request.GET.get("buscar"):
        
        formulario = Busqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            datos2 = Alumnos.objects.filter(codigo__icontains = data["buscar"])
        
        return render(request,'Aplicaciones/a.html', {'datos2':datos2, "formulario" : formulario})
        
    else:
        formulario = Busqueda()
        return render(request,'Aplicaciones/a.html', {'datos2':datos2, "formulario" : formulario})

def formulario_cursos(request):
    if request.method == "POST":

        codigo = request.POST["codigo"]
        nombre = request.POST["nombre"]
        creditos = request.POST["creditos"]
        

        cursos = Cursos(codigo=codigo, nombre=nombre, creditos=creditos)
        cursos.save()
        
        return render(request, "Aplicaciones/index2.html")
    else:
        return render(request, "Aplicaciones/formulario_cursos.html")