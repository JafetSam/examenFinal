from django.contrib import admin
from controlEstudiantes.models import Materia, MateriaAdmin, Grado, GradoAdmin

#Registramos nuestras clases principales.
admin.site.register(Materia,MateriaAdmin)
admin.site.register(Grado, GradoAdmin)
