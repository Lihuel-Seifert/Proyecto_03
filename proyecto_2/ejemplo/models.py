from django.db import models

# Create your models here.
class Producto(models.Model):

    nombre = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    precio = models.FloatField()
    fecha_vencimiento = models.DateField(blank=True, null=True)
    stock = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.marca}" # TODO