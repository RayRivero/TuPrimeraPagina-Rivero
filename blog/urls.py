from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Ruta para la página de inicio
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('agregar_post/', views.agregar_post, name='agregar_post'),
    path('agregar_comentario/<int:post_id>/', views.agregar_comentario, name='agregar_comentario'),
    path('buscar/', views.buscar_post, name='buscar_post'),
    path('post/<int:post_id>/', views.ver_post, name='ver_post'),
    path('post/<int:post_id>/agregar_comentario/', views.agregar_comentario, name='agregar_comentario'),
    path('filtro_categoria/', views.filtro_categoria, name='filtro_categoria'),
]
