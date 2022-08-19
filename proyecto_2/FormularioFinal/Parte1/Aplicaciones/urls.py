from django.urls import path
from Aplicaciones.views import *

urlpatterns = [
    path('', cursos, name='cursos'),
    path('notas/',notas, name='notas' ),
    path('alumnos/', alumnos, name='alumnos'),
    path('formulario_cursos', formulario_cursos, name='formulario_cursos')
]
