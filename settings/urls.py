from rest_framework.routers import DefaultRouter
from .resource import (
    ProvinciaViewSet,
    MunicipioViewSet,
    FechaViewSet,
    GrupoEtarioViewSet,
)

router = DefaultRouter()
router.register(r"fecha", FechaViewSet)
router.register(r"grupo_etario", GrupoEtarioViewSet)
router.register(r"provincias", ProvinciaViewSet)
router.register(r"municipios", MunicipioViewSet)
