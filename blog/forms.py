# blog/forms.py
from django import forms
from .models import Post, Autor, Categoria

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor', 'categoria']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'email']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class BuscarPostForm(forms.Form):
    titulo = forms.CharField(max_length=200, required=False, label='Buscar por título')