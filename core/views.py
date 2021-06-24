from django.shortcuts import render, redirect
from .models import cletaRevision
from core.forms import cletaForm
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UsernameField


# Create your views here.
# Listado de vehiculos

def menu(request):
    
    return render(request,'core/menu.html')


def loginadmin(request):

    if request.method == 'POST':
        
        form = LoginView(request.POST) 
        if UsernameField == 'admin':

            return redirect('menu')


    return render(request,'core/login_adminn.html')

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



def mantenedor(request):
    cletas = cletaRevision.objects.all()

    datos = {
        'cletas':cletas
    }

    return render(request,'core/mantenedorr.html',datos)

def mantenedormod(request,pk):

    cleta = cletaRevision.objects.get(idbicicleta = pk)

    datos = {
        'form':cletaForm(instance=cleta)
    }

    if request.method == 'POST':

        formularioeditado = cletaForm(request.POST,request.FILES,instance=cleta)


        if formularioeditado.is_valid:
            formularioeditado.save()

            datos['mensaje']='Datos actualizados, volver a mantenedor para ver la actualizacion'
        else:
            datos['mensaje']='Hubo algun error intentelo de nuevo '

    return render(request,'core/mantenedormodd.html',datos)


def agregar(request):

    datos = {
        'form':cletaForm()
    }

    if request.method=='POST':
        formularioo = cletaForm(request.POST,request.FILES)
        try:
            if formularioo.is_valid:
                formularioo.save()

                datos['mensaje'] ="guardados correctamente"

        except:
            datos['mensaje'] ="no se pudo guardar"
        

    return render(request,'core/agregar.html',datos)

def delete(request,pk):

    cleta = cletaRevision.objects.get(idbicicleta = pk)

    cleta.delete()

    return redirect(to='mantenedorr')

def login(request):
    return render(request,'core/login.html')


def logout(request):
    return render(request,'core/logout.html')

def formulario_registro(request):
    return render(request,'core/formulario_arriendo.html')


