# blog/views.py
from django.shortcuts import render, redirect
from .models import Post, Autor, Categoria
from .forms import PostForm, AutorForm, CategoriaForm, BuscarPostForm

def index(request):
    return render(request, 'blog/index.html')

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AutorForm()
    return render(request, 'blog/autor_form.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'blog/categoria_form.html', {'form': form})

def buscar_post(request):
    if request.method == 'POST':
        form = BuscarPostForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            posts = Post.objects.filter(titulo__icontains=titulo)
            return render(request, 'blog/buscar.html', {'form': form, 'posts': posts})
    else:
        form = BuscarPostForm()
    return render(request, 'blog/buscar.html', {'form': form})