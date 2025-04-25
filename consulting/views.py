from django.shortcuts import render
from .models import *

# Create your views here.
def consulting (request):
    return render(request, 'consulting/inicioConsultas.html')

def videos_consultoria(request):
    videos = VideoConsultoria.objects.all().order_by('id')
    desbloqueados = videos.filter(models.Q(desbloqueado=True) | models.Q(completado=True)).count()
    total = videos.count()
    progreso = round((desbloqueados / total) * 100) if total > 0 else 0

    return render(request, "consulting/videos.html", {
        "videos": videos,
        "progreso": progreso,
    })
