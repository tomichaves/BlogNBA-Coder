from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # Inicio

    path('post/new', views.post_new, name='post_new'), # Alta Post
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # Detalle Post
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), # Editar Post
    path('post/<pk>/remove/', views.post_remove, name='post_remove'), # Borrar Post

    path('equipos/list', views.equipo_list, name='equipos_list'), # Lista Equipos

    path('equipo/new', views.equipo_new, name='equipos_new'), # Alta Equipo
    path('equipo/<int:pk>/', views.equipo_detail, name='equipos_detail'), # Detalle Equipos
    path('equipo/<int:pk>/edit/', views.equipo_edit, name='equipos_edit'), # Editar Equipos
    path('equipos/<pk>/remove/', views.equipo_remove, name='equipos_remove'), # Borrar Equipos

    path('borrador/', views.post_borrador_list, name='post_borrador_list'), # borradores
    path('post/<pk>/publicar/', views.post_publicar, name='post_publicar'), # Publicar
    
    path('registro/', views.registro, name = 'registro'), # Registrar Usuario
    path('contacto/', views.contacto, name = 'contacto'), # Contacto
    path('Error/', views.Error, name = 'Error'), # Error
    path('about/', views.About, name = 'About'), # About
    
]