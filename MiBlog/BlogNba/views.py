from email import message
from re import template
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.detail import DetailView

def post_list(request):
    posts = Post.objects.filter(fecha_publicado__lte = timezone.now()).order_by('fecha_publicado')
    return render(request, 'BlogNba/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'BlogNba/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'BlogNba/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'BlogNba/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def post_borrador_list(request):
    posts = Post.objects.filter(fecha_publicado__isnull = True).order_by('fecha_creado')
    return render(request, 'BlogNba/post_borrador_list.html', {'posts': posts})

def post_publicar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publicar()
    return redirect('post_detail', pk=pk)

###

def equipo_list(request):
    equipos = Equipos.objects.all()
    return render(request, 'BlogNba/equipos_list.html', {'equipos': equipos})

def equipo_detail(request, pk):
    equipo = get_object_or_404(Equipos, pk=pk)
    return render(request, 'BlogNba/equipos_detail.html', {'equipo': equipo})

def equipo_new(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            equipo = form.save(commit=False)
            equipo.save()
            return redirect('equipos_detail', pk=equipo.pk)
    else:
        form = EquipoForm()
    return render(request, 'BlogNba/equipos_edit.html', {'form': form})

def equipo_edit(request, pk):
    equipo = get_object_or_404(Equipos, pk=pk)
    if request.method == "POST":
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            equipo = form.save(commit=False)
            equipo.save()
            return redirect('equipos_detail', pk=equipo.pk)
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'BlogNba/equipos_edit.html', {'form': form})

def equipo_remove(request, pk):
    equipo = get_object_or_404(Equipos, pk=pk)
    equipo.delete()
    return redirect('equipos_list')

###

def registro(request):
    data = {
        'form': UserCreateForm()
        }

    if request.method == 'POST':
        formulario = UserCreateForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to='post_list')
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

def contacto(request):
    return render(request, 'BlogNba/contact.html', {})

def Error(request):
    return render(request, 'BlogNba/404_Error.html', {})

def About(request):
    return render(request, 'BlogNba/about.html', {})
