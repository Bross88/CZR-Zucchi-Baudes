from turtle import circle
from django.db import models


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



