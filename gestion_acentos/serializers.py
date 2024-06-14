from rest_framework import serializers
from .models import (
    DistAcentCat,
    DistAcentSubCat,
    DistAcentFechaStd,
    DistAcentFechaEval,
)


class DistAcentCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistAcentCat
        fields = "__all__"


class DistAcentSubCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistAcentSubCat
        fields = "__all__"


class DistAcentFechaStdSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistAcentFechaStd
        fields = "__all__"


class DistAcentFechaEvalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistAcentFechaEval
        fields = "__all__"
