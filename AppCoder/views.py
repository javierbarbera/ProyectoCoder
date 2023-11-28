from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante, Entregable, Profesor
from AppCoder.forms import CursoFormulario

# Create your views here.

def mostrar_fecha_actual(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "fecha_actual.html", {"fecha_actual" : fecha_actual})

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def index(request):
    return render(request, "AppCoder/index.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def cursos_formulario(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(curso=informacion["curso"],camada= informacion["camada"])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else: 
        mi_formulario = CursoFormulario()
        return render(request, "AppCoder/cursos_formulario.html", {"mi_formulario": mi_formulario})
    
def buscar_camada(request):
    return render(request, "AppCoder/buscar_camada.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos, "camada": camada})
    else:
        respuesta = "No enviaste datos."
        return render(request, "AppCoder/resultadosBusqueda.html", {"respuesta": respuesta})