from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'contenido','equipo')

class EquipoForm(forms.ModelForm):

    class Meta:
        model = Equipos
        fields = ('ciudad', 'equipo')

class UserCreateForm(UserCreationForm):
    
    class Meta:
        model = User
        fields =  ['username', 'first_name', 'last_name', 'email', 'password1','password2']