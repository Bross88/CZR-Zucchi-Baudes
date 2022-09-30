#from turtle import circle
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User #,AbstractBaseUser,BaseUserManager


#_________________________usuario prueba2 error al usar AUTH_USER_MODEL Ver!!!--------------------------------------------------------------
#______________explorar ORM de Django________________________________________________
"""
class UsuarioManager(BaseUserManager):
    def create_user(self, username,email,pais,last_name,cuit,password = None):
        if not email:
            raise ValueError('Email Requerido!')
        
        usuario =self.model(
            username=username,
            email= self.normalize_email(email),
            pais=pais,
            last_name=last_name,
            cuit=cuit
        )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username,pais,cuit, email, last_name,password):
        usuario = self.create_user(
            email,
            username=username,
            pais=pais,
            last_name=last_name,
            cuit=cuit
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario



class Usuario(AbstractBaseUser):  
    username=models.CharField('Nombre de Usuario' ,max_length=80,unique=True,null=False)
    last_name=models.CharField('Apellido',max_length=100,null=False)
    telefono_movil=models.CharField(max_length=50,null=True,blank=True,unique=True)
    pais=models.CharField(max_length=50)
    email=models.EmailField('Correo Electrinico',max_length=100,unique=True)
    cuit=models.IntegerField(null=True,blank=True,unique=True)
    imagen = models.ImageField(upload_to=None, max_length=200,null=True,blank=True)
    usuario_administrador=models.BooleanField(default=False)
    objects=UsuarioManager()

    USERNAME_FIELD ='username'
    REQUIRED_FIELDS: list['last_name','email','cuit','pais']

    def __str__(self):  
        return f'{self.username},{self.last_name}'

    def has_perm(self,perm,obj = none):
        return True

    def has_module_perms(self,App_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador





"""


#_________________________modelo de registro prueba 2----------------------------------------_______________________________________________________________________________________
"""
class Register(AbstractBaseUser):  
    username=models.CharField('Nombre de Usuario' ,max_length=80,unique=True,null=False)
    last_name=models.CharField('Apellido'max_length=100,null=False)
    telefono_movil=models.CharField(max_length=50,null=True,blank=True,unique=True)
    pais=models.CharField(max_length=50)
    email=models.EmailField('Correo Electrinico'max_length=100,unique=True)
    cuit=models.IntegerField(null=True,blank=True,unique=True)
    usuario_administrador=models.BooleanField(default=False)

    USERNAME_FIELD ='username'
    REQUIRED_FIELDS: list['last_name','email','cuit','pais']

    def __str__(self):  
        return f'{self.username},{self.last_name}'

    def has_perm(self,perm,obj = none):
        return True

    def has_module_perms(self,App_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador


"""



#_______________________________________________MODELO_AVATAR______________________________

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', height_field=None, null=True)