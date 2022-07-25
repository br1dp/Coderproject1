from django.contrib import admin

from app_coder.models import Curso, Entregable, Estudiantes, Profesor

class ProfesorAdmin(admin.ModelAdmin):

    list_display = ("nombre","apellido","profesion","email")
    search_fields = ("nombre","apellido")


admin.site.register(Curso)
admin.site.register(Estudiantes)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Entregable)
