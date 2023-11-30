from django.shortcuts import render
import datetime
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante, Entregable, Profesor
from AppCoder.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario, EntregableFormulario
from django.shortcuts import get_object_or_404
# Create your views here.

def mostrar_fecha_actual(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "fecha_actual.html", {"fecha_actual" : fecha_actual})

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def index(request):
    return render(request, "AppCoder/index.html")

def cursos(request):
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
        return render(request, "AppCoder/cursos.html", {"mi_formulario": mi_formulario})
    
def profesores(request):
    if request.method == "POST":
        mi_formulario = ProfesorFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor = Profesor(nombre=informacion["nombre"],apellido= informacion["apellido"], email= informacion["email"], profesion= informacion["profesion"])
            profesor.save()
            return render(request, "AppCoder/inicio.html")
    else: 
        mi_formulario = ProfesorFormulario()
        return render(request, "AppCoder/profesores.html", {"mi_formulario": mi_formulario})

def estudiantes(request):
    if request.method == "POST":
        mi_formulario = EstudianteFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            estudiante = Estudiante(nombre=informacion["nombre"],apellido= informacion["apellido"], email= informacion["email"])
            estudiante.save()
            return render(request, "AppCoder/inicio.html")
    else: 
        mi_formulario = EstudianteFormulario()
        return render(request, "AppCoder/estudiantes.html", {"mi_formulario": mi_formulario})

def entregables(request):
    if request.method == "POST":
        mi_formulario = EntregableFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            entregable = Entregable(nombre=informacion["nombre"],fecha_entrega=informacion["fecha_entrega"], entregado=informacion["entregado"] )
            entregable.save()
            return render(request, "AppCoder/inicio.html")
    else: 
        mi_formulario = EntregableFormulario()
        return render(request, "AppCoder/entregables.html", {"mi_formulario": mi_formulario})


   
#FORMULARIOS DE BUSQUEDA

def buscar_camada(request):
    return render(request, "AppCoder/buscar_camada.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET["camada"]
        curso = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultadosBusqueda.html", {"curso": curso, "camada": camada})
    else:
        respuesta = "No enviaste datos."
        return HttpResponse(respuesta)

#FORMULARIOS DE LECTURA

def leer_cursos(request):

    curso= Curso.objects.all()  #todos los cursos de la base de datos

    contexto = {"curso": curso}
    return render(request, "AppCoder/leerCursos.html", contexto)


#FORMULARIOS PARA ELIMINAR

def eliminar_curso(request, curso_nombre):
    curso = Curso.objects.get(curso=curso_nombre)
    curso.delete()
    curso= Curso.objects.all()  #todos los cursos de la base de datos

    contexto = {"curso": curso}
    return render(request, "AppCoder/leerCursos.html", contexto)

#FORMULARIOS PARA ACTUALIZAR DATOS

def editar_curso(request, curso_nombre):
    curso = get_object_or_404(Curso, curso=curso_nombre)

    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso.curso = informacion["curso"]
            curso.camada = informacion["camada"]
            
            curso.save()

            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario(initial={"curso": curso.curso, "camada": curso.camada})

    return render(request, "AppCoder/editarCurso.html", {"miFormulario": miFormulario, "curso_nombre": curso_nombre})


