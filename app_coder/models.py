import cmath
from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.nombre} - {self.camada}"

    class Meta():
        verbose_name = "My Course" 
        verbose_name_plural = "Mis Cursos"
        ordering = ("nombre",)
        unique_together = ("nombre","camada")

class Estudiantes(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    profesion = models.CharField( max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido} - {self.profesion} - {self.email}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    FechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    estudiante = models.ForeignKey(Estudiantes,on_delete=models.CASCADE,default=1)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.FechaDeEntrega}"