from rest_framework import routers
from .resources import (
    DistAcentCatRes,
    DistAcentSubCatRes,
    DistAcentFechaStdRes,
    DistAcentFechaEvalRes,
)

router = routers.DefaultRouter()

router.register(r"fecha", DistAcentCatRes)
router.register(r"categoria", DistAcentSubCatRes)
router.register(r"estandand", DistAcentFechaStdRes)
router.register(r"eval", DistAcentFechaEvalRes)
