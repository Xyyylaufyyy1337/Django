from django.shortcuts import render

# Create your views here.
from .models import Write
def index(request):
    return render(request, 'index.html')

def writer(request):
    Writer = {
        'title': 'Kerangka Kerja Django',
        'writer': Write.objects.all()
    }
    return render(request, 'writer.html', Writer)

def about(request):
    return render(request, 'about.html')