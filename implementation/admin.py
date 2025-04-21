from django.contrib import admin
from .models import Servicios, ImplementationRequest

@admin.register(Servicios)
class ServiciosAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  # Solo mostrar el nombre del servicio
    search_fields = ('nombre',)  # Permite buscar por nombre

@admin.register(ImplementationRequest)
class ImplementationRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'servicio', 'status', 'created_at')  # Muestra el servicio y otros campos
    list_filter = ('status', 'servicio')  # Filtro por estado y servicio
    search_fields = ('title', 'description', 'servicio__nombre')  # Búsqueda en título, descripción y nombre del servicio
    ordering = ('-created_at',)  # Ordena por fecha de creación, de más reciente a más antiguo
    readonly_fields = ('created_at',)  # Haz el campo `created_at` solo lectura
