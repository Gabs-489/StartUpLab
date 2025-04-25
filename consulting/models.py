from django.db import models

class VideoConsultoria(models.Model):
    titulo = models.CharField(max_length=255)
    imagen_url = models.CharField(max_length=500)
    descripcion = models.TextField()
    desbloqueado = models.BooleanField(default=False)
    completado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
