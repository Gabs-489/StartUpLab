from django.shortcuts import render

# Create your views here.
def consulting (request):
    return render(request, 'consulting/inicioConsultas.html')
