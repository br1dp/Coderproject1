from django.http import HttpResponse
from django.shortcuts import render
from app_coder.forms import CursoFormulario


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


# def cursoformulario(request):

#     print("method:",request.method)
#     print("request:",request.POST)

#     if request.method == "POST":

#         curso = Curso(nombre = request.POST["Cursos"],camada = request.POST["Camada"])

#         curso.save()

   
#         return render(request,"inicio.html")
        
#     return render(request,"cursoformulario.html")

def cursoformulario(request):

    print("method:",request.method)
    print("request:",request.POST)

    if request.method == "POST":

        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

        curso = Curso(nombre = data["curso"],camada = data["camada"])

        curso.save()

   
        return render(request,"inicio.html")
    else:
        miFormulario = CursoFormulario()

    return render(request,"cursoformulario.html",{"miFormulario":miFormulario})

