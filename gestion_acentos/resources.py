from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    DistAcentCat,
    DistAcentSubCat,
    DistAcentFechaStd,
    DistAcentFechaEval,
)
from .serializers import (
    DistAcentCatSerializer,
    DistAcentSubCatSerializer,
    DistAcentFechaStdSerializer,
    DistAcentFechaEvalSerializer,
)


class DistAcentCatRes(viewsets.ModelViewSet):
    queryset = DistAcentCat.objects.all()
    serializer_class = DistAcentCatSerializer
    permission_classes = [IsAuthenticated]


class DistAcentSubCatRes(viewsets.ModelViewSet):
    queryset = DistAcentSubCat.objects.all()
    serializer_class = DistAcentSubCatSerializer
    permission_classes = [IsAuthenticated]


class DistAcentFechaStdRes(viewsets.ModelViewSet):
    queryset = DistAcentFechaStd.objects.all()
    serializer_class = DistAcentFechaStdSerializer
    permission_classes = [IsAuthenticated]


class DistAcentFechaEvalRes(viewsets.ModelViewSet):
    queryset = DistAcentFechaEval.objects.all()
    serializer_class = DistAcentFechaEvalSerializer
    permission_classes = [IsAuthenticated]
