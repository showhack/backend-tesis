from django.db import models

from gestion_miembros.models import Entrenador
from settings.models import Fecha


# class DistribucionVolSemNXContenidoFecha(models.Model):
#     mes = models.CharField(max_length=100)
#     semana = models.IntegerField()
#     anno = models.IntegerField()


class DistVolSemContCualidad(models.Model):
    nombre = models.CharField(max_length=255)
    # grupo_etario = models.ManyToManyField("gestion_miembros.GrupoEtario")


class DistVolSemContCualFechaStd(models.Model):
    # almacena la distribucion estandard
    marcado = models.BooleanField(default=False)
    porciento = models.DecimalField(max_digits=5, decimal_places=2)
    cualidad = models.ForeignKey(DistVolSemContCualidad, on_delete=models.CASCADE)
    fecha = models.ForeignKey(Fecha, on_delete=models.CASCADE)


class DistVolSemNXContCualFechaEval(models.Model):
    # Esta tabla almacena la distribucion hecha por el entrenador...
    marcado = models.BooleanField(default=False)
    porciento = models.DecimalField(max_digits=5, decimal_places=2)
    cualidad = models.ForeignKey(DistVolSemContCualidad, on_delete=models.CASCADE)
    fecha = models.ForeignKey(Fecha, on_delete=models.CASCADE)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True)
