from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, NotaAlumnoCursoForm

def nuevo_alumno(request):
    form = AlumnoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('nuevo_alumno')
    return render(request, 'colegio/formulario.html', {'form': form, 'titulo': 'Nuevo Alumno'})

def nuevo_curso(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('nuevo_curso')
    return render(request, 'colegio/formulario.html', {'form': form, 'titulo': 'Nuevo Curso'})

def nueva_nota(request):
    form = NotaAlumnoCursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('nueva_nota')
    return render(request, 'colegio/formulario.html', {'form': form, 'titulo': 'Nueva Nota'})
