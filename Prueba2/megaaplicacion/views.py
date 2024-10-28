from django.shortcuts import render
from megaaplicacion.form import FormProyecto
from megaaplicacion.models import Proyecto


def index(request):
    
    return render(request,"templatesApp/index.html")

def lista(request):
    proyectos = Proyecto.objects.all()
    data = {"proyectos": proyectos}
    return render(request,"templatesApp/lista.html",data)

def agregar(request):
    form = FormProyecto()
    if request.method == "POST":
        form = FormProyecto(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = { "form": form}
    return render(request,"templatesApp/agregar.html",data)