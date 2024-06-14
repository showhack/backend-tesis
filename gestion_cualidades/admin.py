from django.contrib import admin
from .models import (
    # DistribucionVolSemNXContenidoFecha,
    DistVolSemContCualidad,
    DistVolSemContCualFechaStd,
    DistVolSemNXContCualFechaEval,
)


# @admin.register(DistribucionVolSemNXContenidoFecha)
# class DistribucionVolSemNXContenidoFechaAdmin(admin.ModelAdmin):
#     list_display = ("mes", "semana", "anno")
#     search_fields = ("mes", "semana", "anno")


@admin.register(DistVolSemContCualidad)
class DistribucionVolSemNXContenidoCualidadAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(DistVolSemContCualFechaStd)
class DistribucionVolSemNXContenidoCualidadRelFechaEstandardAdmin(admin.ModelAdmin):
    list_display = ("marcado", "porciento", "cualidad", "fecha")
    search_fields = ("cualidad__nombre", "fecha__mes", "fecha__semana")
    list_filter = ("marcado", "fecha", "cualidad")


@admin.register(DistVolSemNXContCualFechaEval)
class DistribucionVolSemNXContenidoCualidadRelFechaEvalAdmin(admin.ModelAdmin):
    list_display = ("marcado", "porciento", "cualidad", "fecha", "entrenador")
    search_fields = (
        "cualidad__nombre",
        "fecha__mes",
        "fecha__semana",
        "fecha__anno",
        "entrenador__nombre",
    )
    list_filter = ("marcado", "fecha", "cualidad", "entrenador")
