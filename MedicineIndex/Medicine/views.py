from django.shortcuts import render
from .models import Medicine
# Create your views here.

def index(request):
    medicines = Medicine.objects.all()
    return render(request, 'index.html')

def search(request):
    return render(request, 'index.html')

def medicine_detail(request, pk):
    return render(request, 'index.html')

def medicine_create(request):
    return render(request, 'index.html')

def medicine_edit(request, pk):
    return render(request, 'index.html')

def medicine_delete(request, pk):
    return render(request, 'index.html')
