from django.urls import path
from AppCoder import views

urlpatterns = [
    path("fecha-actual", views.mostrar_fecha_actual, name= "mostrar_fecha_actual"),
    path("inicio/", views.inicio, name="inicio"),
    path("cursos/", views.cursos, name="cursos"),
    path("profesores/", views.profesores, name="profesores"),
    path("estudiantes/", views.estudiantes, name="estudiantes"),
    path("entregables/", views.entregables, name="entregables"),
    path("cursosFormulario/", views.cursos_formulario, name="cursos_formulario"),
    path("buscarCamada/", views.buscar_camada, name="buscar_camada"),
    path("buscar/", views.buscar),
    path("index/", views.index),
]