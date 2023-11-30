from django.urls import path
from AppCoder import views

urlpatterns = [
    path("fecha-actual", views.mostrar_fecha_actual, name= "mostrar_fecha_actual"),
    path("inicio/", views.inicio, name="inicio"),
    path("cursos/", views.cursos, name="cursos"),
    path("profesores/", views.profesores, name="profesores"),
    path("estudiantes/", views.estudiantes, name="estudiantes"),
    path("entregables/", views.entregables, name="entregables"),
    #path("cursosFormulario/", views.cursos_formulario, name="cursos_formulario"),
    path("buscarCamada/", views.buscar_camada, name="buscar_camada"),
    path('buscar/', views.buscar, name="buscar"),
    #path("estudianteFormulario/", views.estudiante_formulario, name="estudiante_formulario"),
    #path("profesorFormulario/", views.profesor_formulario, name="profesor_formulario"),
    #path("entregableFormulario/", views.entregable_formulario, name="entregable_formulario"),
    path('leerCursos/', views.leer_cursos, name= "leerCursos"),
    path('EliminarCurso/<curso_nombre>/', views.eliminar_curso, name= "EliminarCurso"),
    path('editarCurso/<curso_nombre>/', views.editar_curso, name= "EditarCurso"),
    path("index/", views.index),
]