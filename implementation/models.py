from django.db import models

# Create your models here.

class Servicios(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class ImplementationRequest(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'Esperando'),
        ('pending', 'Pendiente'),
        ('resolved', 'Resuelta'),
    ]
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"


