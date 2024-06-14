from rest_framework import serializers
from .models import Provincia, Municipio, Fecha, GrupoEtario


class FechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fecha
        fields = "__all__"


class GrupoEtarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoEtario
        fields = "__all__"


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = "__all__"


class ProvinciaSerializer(serializers.ModelSerializer):
    municipios = MunicipioSerializer(many=True, read_only=True)

    class Meta:
        model = Provincia
        fields = "__all__"
