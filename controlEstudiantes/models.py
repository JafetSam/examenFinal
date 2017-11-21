from django.db import models
from django.contrib import admin

# Create your models here.


class Materia(models.Model):
    nombre=models.CharField(max_length=30)
    def __str__(self):
        return self.nombre


class Grado(models.Model):
    nombre  =   models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    materias= models.ManyToManyField(Materia, through='Gradomaterias')

    def __str__(self):
        return self.nombre


class Gradomaterias (models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)



class GradoInLine(admin.TabularInline):
    model = Gradomaterias
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1


class MateriaAdmin(admin.ModelAdmin):
    inlines = (GradoInLine,)


class GradoAdmin (admin.ModelAdmin):
    inlines = (GradoInLine,)
