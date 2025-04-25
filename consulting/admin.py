from django.contrib import admin
from .models import VideoConsultoria

@admin.register(VideoConsultoria)
class VideoConsultoriaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "desbloqueado", "completado")
    list_filter = ("desbloqueado", "completado")
    search_fields = ("titulo", "descripcion")
