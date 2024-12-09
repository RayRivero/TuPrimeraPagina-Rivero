from django import forms
from .models import Categoria, Post, Comentario

# Formulario para la categoría
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

# Formulario para el post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'categoria']

# Formulario para el comentario
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre_usuario', 'contenido']