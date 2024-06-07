from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from gestion_miembros.urls import router as gestion_miembros_routes
from gestion_cualidades.urls import router as gestion_cualidades_routes

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
                    "gestion_miembros/",
                    include(gestion_miembros_routes.urls),
                    name="gestion_miembros",
                ),
                path(
                    "gestion_cualidades/",
                    include(gestion_cualidades_routes.urls),
                    name="cualidades",
                ),
            ]
        ),
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
