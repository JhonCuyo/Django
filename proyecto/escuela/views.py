from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, NotaForm

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_alumno')
    else:
        form = AlumnoForm()
    return render(request, 'agregar_alumno.html', {'form': form})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_curso')
    else:
        form = CursoForm()
    return render(request, 'agregar_curso.html', {'form': form})

