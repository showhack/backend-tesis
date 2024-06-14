from django.db import models
from gestion_miembros.models import Entrenador
from settings.models import Fecha


class DistAcentCat(models.Model):
    nombre = models.CharField(max_length=100)  # almacena las categorias

    def __str__(self):
        return self.nombre


class DistAcentSubCat(models.Model):
    nombre = models.CharField(max_length=100)  # Almacena las subcategorias
    categoria = models.ForeignKey(DistAcentCat, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    # grupo_etario = models.ManyToManyField("gestion_miembros.GrupoEtario")
    # entrenador = models.ManyToManyField("gestion_miembros.Entrenador")
    # instructor = models.ManyToManyField("gestion_miembros.Instructor")


class DistAcentFechaStd(models.Model):
    cualidad = models.ForeignKey(DistAcentSubCat, on_delete=models.CASCADE)
    prioridad = models.CharField(
        max_length=20,
        choices=[
            ("MIN", "MIN"),
            ("MED", "MED"),
            ("MAX", "MAX"),
        ],
    )
    fecha = models.ForeignKey(Fecha, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cualidad} - {self.fecha}"


class DistAcentFechaEval(models.Model):
    cualidad = models.ForeignKey(DistAcentSubCat, on_delete=models.CASCADE)
    prioridad = models.CharField(
        max_length=20,
        choices=[
            ("MIN", "MIN"),
            ("MED", "MED"),
            ("MAX", "MAX"),
        ],
    )
    fecha = models.ForeignKey(Fecha, on_delete=models.CASCADE)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.cualidad} - {self.fecha}"
