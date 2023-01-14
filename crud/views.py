from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from crud.form import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def crud(request):
    remedio = remedios.objects.all()
    form = remediosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("crud")

    pacote = {"chave": remedio, "form":form}

    return render(request, 'crud.html', pacote)

def read(request):
    remedio = remedios.objects.all()
    pacote = {"chave": remedio}
    return render(request, 'read.html', pacote)

def search(request):
    return render(request, 'search.html')

def update(request, id_remedio):
    remedio = remedios.objects.get(pk = id_remedio)
    form = remediosForm(request.POST or None, instance = remedio)
    if form.is_valid():
        form.save()
        return redirect("crud")
    
    pacote = {"form": form}

    return render(request, 'update.html', pacote)

def delete(request, id_remedio):
    remedio = remedios.objects.get(pk = id_remedio)
    remedio.delete()
    return redirect("crud")
