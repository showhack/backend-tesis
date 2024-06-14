from django.db import models


# Create your models here.
class Fecha(models.Model):
    fecha = models.CharField(max_length=100)
    semana = models.IntegerField()
    mes = models.CharField(max_length=100)
    anno = models.CharField(max_length=50)

    def __str__(self):
        return self.fecha

class GrupoEtario(models.Model):
    nombre = models.CharField(max_length=150)

class Provincia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(
        Provincia, related_name="municipios", on_delete=models.CASCADE
    )

    def __str(self):
        return self.nombre




# TODO 2.5 Migraciones y MAkemigration


# TODO 3 Buscar como implementar un cron o job como quiera que se llame en django como funciona y donde se hacen (es para tareas automaticas, como llenar una ves al agno el modelo de las fechas). (Youtube)
# TODO 4 Buscar como implementar Tests (ChatGPT)
# TODO 5 Buscar como implementar (django-guardian) para permisos personalizados desde el panel de admin de Django (Youtube)
# TODO 5 Definir de los urls (endpoints) del swagger las que no merezcan su existencia (ver como se hace en .ignore/permissions.py)
