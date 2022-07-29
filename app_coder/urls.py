
from django.urls import path

from app_coder.views import curso, cursoformulario, cursos, entregables, estudiante, inicio, profesores,buscar, busquedaCamada



urlpatterns = [
    path('agregacurso/<nombre>/<camada>', curso),
    path('cursos/', cursos, name ="Cursos"),
    path('estudiantes/', estudiante, name = "Estudiantes"),
    path('entregables/',entregables, name = "Entregables"),
    path('profesores/',profesores, name = "Profesores"),
    path('', inicio, name = "Inicio"),
    path('cursoformulario/', cursoformulario, name = "CursoFormulario"),
    path('busquedaCamada/', busquedaCamada, name = "BusquedaCamada"),
    path('buscar/', buscar, name = "Buscar"),
    
    
]
