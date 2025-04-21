from django import forms
from .models import ImplementationRequest, Servicios

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ['nombre']  

class ImplementationRequestForm(forms.ModelForm):
    class Meta:
        model = ImplementationRequest
        fields = ['servicio', 'title', 'description']
        widgets = {
            'servicio': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'servicio': 'Selecciona un servicio',
            'title': 'Título de la solicitud',
            'description': 'Descripción',
        }