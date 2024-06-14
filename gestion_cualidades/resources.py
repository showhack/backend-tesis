from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    DistVolSemContCualidad,
    DistVolSemContCualFechaStd,
    DistVolSemNXContCualFechaEval,
)
from .serializers import (
    # DistribucionVolSemNXContenidoFechaSerializer,
    DistVolSemNXContCualidadSerializer,
    DistVolSemNXContCualFechaStdSerializer,
    DistVolSemNXContCualFechaEvalSerializer,
)


class DistVolSemNXContCualRes(viewsets.ModelViewSet):
    queryset = DistVolSemContCualidad.objects.all()
    serializer_class = DistVolSemNXContCualidadSerializer
    permission_classes = [IsAuthenticated]


class DistVolSemNXContCualFechaStdRes(viewsets.ModelViewSet):
    queryset = DistVolSemContCualFechaStd.objects.all()
    serializer_class = DistVolSemNXContCualFechaStdSerializer
    permission_classes = [IsAuthenticated]


class DistVolSemNXContCualFechaEvalRes(viewsets.ModelViewSet):
    queryset = DistVolSemNXContCualFechaEval.objects.all()
    serializer_class = DistVolSemNXContCualFechaEvalSerializer
    permission_classes = [IsAuthenticated]
