from django.urls import path
from .views import formulario_registro, menu,registro,login,logout,mantenedor,mantenedormod,agregar,delete
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',menu, name="menu"),    
    path('registro/',registro,name="registro"),
    path('login/',LoginView.as_view(template_name='core/login.html'),name="login"),
    path('logout/',LogoutView.as_view(template_name='core/logout.html'),name="logout"),
    path('formulario_registro',formulario_registro,name="formulario_registro"),
    path('login_adminn/',LoginView.as_view(template_name='core/login_adminn.html'),name="login_adminn"),
    path('mantenedorr/',mantenedor,name="mantenedorr"),
    path('mantenedormodd/<pk>',mantenedormod,name="mantenedormod"),
    path('agregar/',agregar,name="agregar"),
    path('delete/<pk>/',delete,name="delete"),

]