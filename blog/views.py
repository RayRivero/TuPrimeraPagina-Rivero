from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Categoria, Post, Comentario
from .forms import CategoriaForm, PostForm, ComentarioForm
from django.db.models import Q

# Vista para la página de inicio
def inicio(request):
    # Mostrar todos los posts en la página principal
    posts = Post.objects.all()
    return render(request, 'blog/inicio.html', {'posts': posts})

# Vista para agregar una nueva categoría
def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            # Verificar si la categoría ya existe
            categoria_nombre = form.cleaned_data['nombre']
            if Categoria.objects.filter(nombre=categoria_nombre).exists():
                messages.error(request, '¡La categoría ya existe!')  # Mostrar un mensaje de error si existe
            else:
                form.save()
                messages.success(request, 'Categoría guardada con éxito.')  # Mostrar un mensaje de éxito si se guarda
                return redirect('inicio')  # Redirige a la página principal después de guardar
    else:
        form = CategoriaForm()

    return render(request, 'blog/agregar_categoria.html', {'form': form})

# Vista para agregar un nuevo post
def agregar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_post')  # Redirige después de guardar
    else:
        form = PostForm()
    return render(request, 'blog/agregar_post.html', {'form': form})

# Vista para agregar un comentario a un post
def agregar_comentario(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Obtener el post correspondiente
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post  # Asocia el comentario con el post
            comentario.save()
            messages.success(request, 'Comentario agregado con éxito.')
            return redirect('ver_post', post_id=post.id)
        else:
            messages.error(request, 'Hubo un error al agregar el comentario. Intenta de nuevo.')
    else:
        form = ComentarioForm()
    return render(request, 'blog/agregar_comentario.html', {'form': form, 'post': post})

# Vista para buscar publicaciones
def buscar_post(request):
    query = request.GET.get('q', '')  # Obtener el término de búsqueda
    posts = Post.objects.all()  # Inicialmente, obtener todos los posts
    error_message = None  # Variable para almacenar un mensaje de error

    if query:  # Si hay un término de búsqueda
        if len(query) >= 5:  # Validar que la búsqueda tenga al menos 5 caracteres
            posts = posts.filter(Q(titulo__icontains=query) | Q(contenido__icontains=query))
        else:
            error_message = "La búsqueda debe tener al menos 5 caracteres."

    return render(request, 'blog/buscar_post.html', {'posts': posts, 'query': query, 'error_message': error_message})

# Vista para filtrar por categoría
def filtro_categoria(request):
    categoria_id = request.GET.get('categoria', None)
    categorias = Categoria.objects.all()
    posts = Post.objects.filter(categoria=categoria_id) if categoria_id else Post.objects.all()
    
    return render(request, 'blog/filtro_categoria.html', {
        'posts': posts,
        'categorias': categorias,
        'categoria_id': categoria_id,
    })

# Vista para ver un post específico
def ver_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = post.comentarios.all()  # Obtener todos los comentarios asociados al post
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post  # Asociar el comentario con el post
            comentario.save()
            messages.success(request, 'Comentario agregado con éxito.')
            return redirect('ver_post', post_id=post.id)  # Redirigir al mismo post
    else:
        form = ComentarioForm()  # Si no es un POST, mostrar un formulario vacío

    return render(request, 'blog/ver_post.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form,
    })
