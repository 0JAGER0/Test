from django import forms
from django.forms import ModelForm
from .models import registroUsuario,arriendoCleta,cletaRevision
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#Crear la calse para el formulario


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirma contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}

class FormularioRegistro(ModelForm):
    class Meta:
        model = registroUsuario
        fields = ['usuario','nombres','apellidos','correo','contraseña']
        

class cletaForm(ModelForm):
    class Meta:
        model = cletaRevision
        fields = ['idbicicleta','modelo','porte','aro','marca','stock','estado']


class arriendoForm(ModelForm):
    class Meta:
        model = arriendoCleta
        fields = ['idbicicleta','modelo','porte','aro','marca']