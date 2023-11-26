from django.urls import path
from AppCoder import views

urlpatterns = [
    path("fecha-actual", views.mostrar_fecha_actual, name= "mostrar_fecha_actual"),
    path("inicio", views.inicio),
    path("cursos", views.cursos, name= "Cursos"),
    path("profesores", views.profesores),
    path("estudiantes", views.estudiantes),
    path("entregables", views.entregables),
    path("index", views.index),
]