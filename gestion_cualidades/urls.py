from rest_framework import routers
from .resources import (
    DistVolSemNXContCualRes,
    DistVolSemNXContCualFechaStdRes,
    DistVolSemNXContCualFechaEvalRes,
)

router = routers.DefaultRouter()
router.register(r"cualidad", DistVolSemNXContCualRes)
router.register(r"estandand", DistVolSemNXContCualFechaStdRes)
router.register(r"eval", DistVolSemNXContCualFechaEvalRes)
