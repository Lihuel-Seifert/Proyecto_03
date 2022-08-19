from django.db import models

# Create your models here.
class Cursos(models.Model):

    codigo=models.CharField(max_length=6)
    nombre=models.CharField(max_length=50)  
    creditos=models.IntegerField()

class Notas(models.Model):

    codigo=models.IntegerField()
    nombre=models.CharField(max_length=50)
    creditos=models.IntegerField()

class Alumnos(models.Model):

    codigo=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    creditos=models.IntegerField()
            