from django.shortcuts import render, get_object_or_404, redirect
from .models import Autor
from .forms import AutorForm

def index(request):
    autores = Autor.objects.all()
    return render(request, 'app_autores/index.html', {'autores': autores})

def add(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app_autores/add.html', {'form': AutorForm(), 'success': True})
    else:
        form = AutorForm()
    return render(request, 'app_autores/add.html', {'form': form})

def edit(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return render(request, 'app_autores/edit.html', {'form': form, 'success': True})
    else:
        form = AutorForm(instance=autor)
    return render(request, 'app_autores/edit.html', {'form': form})

def delete(request, pk):
    if request.method == 'POST':
        autor = get_object_or_404(Autor, pk=pk)
        autor.delete()
        return redirect('index')
