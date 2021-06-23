from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
# Listado de vehiculos

def menu(request):
    
    return render(request,'core/menu.html')

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado')
            return redirect('menu')
    else:
        form = UserRegisterForm()

    context = { 'form': form }

    return render(request,'core/registro.html',context)

def login(request):
    return render(request,'core/login.html')


def logout(request):
    return render(request,'core/logout.html')

def formulario_registro(request):
    return render(request,'core/formulario_arriendo.html')


