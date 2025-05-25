from django.contrib import admin
from .models import Alumno, Curso, NotaAlumnoCurso

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(NotaAlumnoCurso)