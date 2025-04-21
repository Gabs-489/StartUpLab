from django.shortcuts import redirect, render

from .models import ImplementationRequest

from .forms import ImplementationRequestForm

# Create your views here.
def implementation (request):
    return render(request, 'implementation/inicioImplementacion.html')


def pedidos(request):
    if request.method == 'POST':
        form = ImplementationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedidos')
    else:
        form = ImplementationRequestForm()
    
    waiting = ImplementationRequest.objects.filter(status='waiting').order_by('-created_at')

    pending = ImplementationRequest.objects.filter(status='pending').order_by('-created_at')

    resolved = ImplementationRequest.objects.filter(status='resolved').order_by('-created_at')

    return render(request, 'implementation/pedidos.html', {
        'form': form,
        'waiting':waiting,
        'pending':pending,
        'requests': resolved
    })
