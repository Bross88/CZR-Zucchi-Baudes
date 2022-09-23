from turtle import circle
from django.db import models
from django.contrib.auth.models import User


#modelo de registro prueba 2--------------------------------------------------------------


class Register(models.Model):  
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    telefono_movil=models.CharField(max_length=50,null=True,blank=True)
    pais=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    cuit=models.IntegerField(null=True,blank=True)
    password=models.CharField(max_length=40)
    


    def __str__(self):  
        return self.nombre + " " + self.apellido


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)

