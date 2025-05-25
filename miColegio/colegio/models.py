from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class NotaAlumnoCurso(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        unique_together = ('alumno', 'curso')  # evita duplicados

    def __str__(self):
        return f"{self.alumno} - {self.curso}: {self.nota}"