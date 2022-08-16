
from django.urls import path
from .views import CursoCreate, CursoDelete, CursoDetail, CursoList, CursoUpdate, crearprofesores, editarprofesor, eliminarprofesor, listaprofesores

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
    path('listaProfesores/', listaprofesores, name = "ListaProfesores"),
    path('creaprofesor/', crearprofesores, name = "CreaProfesor"),
    path('eliminarprofesor/<int:id>', eliminarprofesor, name = "EliminaProfesor"),
    path('editarprofesor/<int:id>', editarprofesor, name = "EditarProfesor"),
    path('ListaCursos/', CursoList.as_view(), name = "ListaCursos"),
    path('detalleCursos/<int:pk>', CursoDetail.as_view(), name = "DetalleCursos"),
    path('crearCursos/', CursoCreate.as_view(), name = "CreaCursos"),
    path('actualizarCursos/<int:pk>', CursoUpdate.as_view(), name = "ActualizarCursos"),
    path('eliminarCursos/<int:pk>', CursoDelete.as_view(), name = "EliminarCursos"),
    
    
]
