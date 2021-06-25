from django.db import models

# Create your models here.

#Modelo para categoria

        
class arriendoCleta(models.Model):
    idbicicleta = models.AutoField(primary_key=True, verbose_name="id bicicleta")
    modelo = models.CharField(max_length=50,verbose_name="Modelo bicicleta")
    porte = models.CharField(max_length=30, verbose_name="porte bicicleta")
    aro = models.IntegerField(verbose_name="aro de rueda")
    marca = models.CharField(max_length=50  ,verbose_name="marca bicicleta")
    

    def __str__(self):
        return f'{self.idbicicleta}, {self.modelo}'

class registroUsuario(models.Model):
    usuario = models.CharField(primary_key=True,max_length=50,verbose_name="Nombre Usuario")
    nombres = models.CharField(max_length=70,verbose_name="Nombre")
    apellidos = models.CharField(max_length=70,verbose_name="Apellido")
    correo = models.EmailField(verbose_name="Correo")
    contraseña = models.CharField(max_length=30,verbose_name="Contraseña")

    def __str__(self):
        return self.usuario



class cletaRevision(models.Model):
    idbicicleta = models.AutoField(primary_key=True, verbose_name="id bicicleta")
    modelo = models.CharField(max_length=50,verbose_name="modelo")
    porte = models.CharField(max_length=30, verbose_name="porte")
    aro = models.IntegerField(verbose_name="aro de rueda")
    marca = models.CharField(max_length=50  ,verbose_name="marca bicicleta")
    stock = models.IntegerField( verbose_name="stock")
    estado = models.CharField(max_length=50  ,verbose_name="estado")

    def __str__(self):
        return f'{self.idbicicleta}, {self.modelo}'

