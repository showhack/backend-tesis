from django.contrib import admin
from .models import DistAcentCat, DistAcentSubCat, DistAcentFechaStd, DistAcentFechaEval


@admin.register(DistAcentCat)
class DistAcentCatAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(DistAcentSubCat)
class DistAcentSubCatAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria")
    search_fields = ("nombre", "categoria__nombre")
    list_filter = ("categoria",)


@admin.register(DistAcentFechaStd)
class DistAcentFechaStdAdmin(admin.ModelAdmin):
    list_display = ("cualidad", "prioridad", "fecha")
    search_fields = ("cualidad__nombre", "fecha__fecha")
    list_filter = ("prioridad", "fecha")


@admin.register(DistAcentFechaEval)
class DistAcentFechaEvalAdmin(admin.ModelAdmin):
    list_display = ("cualidad", "prioridad", "fecha", "entrenador")
    search_fields = ("cualidad__nombre", "fecha__fecha", "entrenador__nombre")
    list_filter = ("prioridad", "fecha", "entrenador")
