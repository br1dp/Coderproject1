from django.http import HttpResponse
from django.shortcuts import render

from app_coder.models import Curso

# Create your views here.

def curso(self,nombre , camada):

    curso = Curso (nombre = nombre, camada = camada)
    curso.save()

    return HttpResponse(f"""
    
    <p>
    
    Curso : {curso.nombre} - Camada: {curso.camada} agregada
    
    </p>
    
    """)

def inicio (self):

    return render(self,"inicio.html")

def estudiante (self):

    return render(self,"estudiantes.html")

def profesores (self):

    return render(self,"profesores.html")

def cursos (self):

    return render(self,"cursos.html")

def entregables (self):

    return render(self,"entregables.html")
