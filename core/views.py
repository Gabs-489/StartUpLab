from django.shortcuts import render
from datetime import datetime


def index (request):
    return render(request, 'core/index.html', {
        'current_year': datetime.now().year,
    })
