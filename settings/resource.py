from rest_framework import viewsets
from .models import Provincia, Municipio, Fecha, GrupoEtario
from .serializers import (
    ProvinciaSerializer,
    MunicipioSerializer,
    FechaSerializer,
    GrupoEtarioSerializer,
)


class FechaViewSet(viewsets.ModelViewSet):
    queryset = Fecha.objects.all()
    serializer_class = FechaSerializer


class GrupoEtarioViewSet(viewsets.ModelViewSet):
    queryset = GrupoEtario.objects.all()
    serializer_class = GrupoEtarioSerializer


class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer


class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
