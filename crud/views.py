from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def crud(request):
    return render(request, 'crud.html')

def read(request):
    return render(request, 'read.html')

def search(request):
    return render(request, 'search.html')

def update(request):
    return render(request, 'update.html')