
from django.urls import path
from app_coder.views import curso, cursos, entregables, estudiante, inicio, profesores



urlpatterns = [
    path('agregacurso/<nombre>/<camada>', curso),
    path('cursos/', cursos),
    path('estudiantes/', estudiante),
    path('entregables/',entregables),
    path('profesor/',profesores),
    path('', inicio),
]
