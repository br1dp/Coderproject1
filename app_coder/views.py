from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from .forms import ProfesorFormulario
from .models import Profesor
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

def busquedaCamada(request):

    return render(request,'busquedaCamada.html')
    


def buscar(request):

    if request.GET['camada']:

        camada = request.GET['camada']

        nombre = Curso.objects.filter(camada__icontains=camada)

        return render(request,'resultadoBusqueda.html',{'cursos':nombre,'camada':camada})
    
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

def listaprofesores(request):

    profesores = Profesor.objects.all()

    context = {"profesores":profesores}

    return render (request,"leerProfesores.html",context)

def crearprofesores(request):

    print("method:",request.method)
    print("request:",request.POST)

    if request.method == "POST":

        miFormulario = ProfesorFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

        profesor = Profesor(nombre = data["nombre"],apellido = data["apellido"],email = data["email"],profesion = data["profesion"])

        profesor.save()

   
        return render(request,"inicio.html")
    else:
        miFormulario = ProfesorFormulario()

    return render(request,"profesorformulario.html",{"miFormulario":miFormulario})


def eliminarprofesor(request,id):

    if request.method == "POST":

        profesor = Profesor.objects.get(id = id)

        profesor.delete()

        profesores = Profesor.objects.all()

        context = {"profesores":profesores}

        return render (request,"leerProfesores.html",context)

def editarprofesor(request,id):

    print("method:",request.method)
    print("request:",request.POST)

    profesor = Profesor.objects.get(id = id)

    if request.method == "POST":

        miFormulario = ProfesorFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

        profesor.nombre = data['nombre']
        profesor.apellido = data['apellido']
        profesor.email = data['email']
        profesor.profesion = data['profesion']

        profesor.save()

   
        return render(request,"inicio.html")

    else:

        miFormulario = ProfesorFormulario(initial={
            'nombre': profesor.nombre,
            'apellido': profesor.apellido,
            'email': profesor.email,
            'profesion': profesor.profesion,
        })

    return render(request,"editarProfesor.html",{"miFormulario":miFormulario,'id':profesor.id})

class CursoList(ListView):

    model = Curso

    template_name = "curso_list.html"
    context_object_name = "cursos"

class CursoDetail(DetailView):

    model = Curso

    template_name = "curso_detail.html"

    context_object_name =  "curso"



class CursoCreate(CreateView):

    model = Curso

    template_name = "curso_create.html"

    fields = ['nombre','camada']

    success_url = '/app_coder/'

class CursoUpdate(UpdateView):

    model = Curso

    template_name = "curso_update.html"

    fields = ('__all__')

    success_url = '/app_coder/'
class CursoDelete(DeleteView):

    model = Curso

    template_name = "curso_delete.html"

    success_url = '/app_coder/'
