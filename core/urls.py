from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from settings.urls import router as settings_routes
from gestion_miembros.urls import router as gestion_miembros_routes
from gestion_cualidades.urls import router as gestion_cualidades_routes
from gestion_acentos.urls import router as gestion_acentos_routes


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/doc/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema")),
    path(
        "api/v1/",
        include(
            [
                path("auth/", include("authentication.urls")),
                path(
                    "settings/",
                    include(settings_routes.urls),
                    name="settings",
                ),
                path(
                    "miembros/",
                    include(gestion_miembros_routes.urls),
                    name="miembros",
                ),
                path(
                    "gestion-cualidades/",
                    include(gestion_cualidades_routes.urls),
                    name="gestion-cualidades",
                ),
                path(
                    "gestion-acentos/",
                    include(gestion_acentos_routes.urls),
                    name="gestion-acentos",
                ),
            ]
        ),
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
