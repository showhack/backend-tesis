from rest_framework import serializers
from .models import (
    # DistribucionVolSemNXContenidoFecha,
    DistVolSemContCualidad,
    DistVolSemContCualFechaStd,
    DistVolSemNXContCualFechaEval,
)


# class DistribucionVolSemNXContenidoFechaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DistribucionVolSemNXContenidoFecha
#         fields = "__all__"


class DistVolSemNXContCualidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistVolSemContCualidad
        fields = "__all__"


class DistVolSemNXContCualFechaStdSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistVolSemContCualFechaStd
        fields = "__all__"


class DistVolSemNXContCualFechaEvalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistVolSemNXContCualFechaEval
        fields = "__all__"
