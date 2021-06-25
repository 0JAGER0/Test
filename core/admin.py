from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import cletaRevision, registroUsuario,arriendoCleta

# Register your models here.

admin.site.register(cletaRevision)
admin.site.register(registroUsuario)
admin.site.register(arriendoCleta)