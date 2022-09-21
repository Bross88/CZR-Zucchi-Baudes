from django.db import models


class Monotributista(models.Model):
    categoria = models.CharField(max_length=30,)
    nombre = models.CharField(max_length=30,)
    apellido = models.CharField(max_length=30,)
    edad = models.PositiveIntegerField()
    mail = models.EmailField(max_length=50)  #verbose_name='email',
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Categoria: {self.categoria}, mail: {self.mail}"
    
    
class ResponsableInscripto(models.Model):
    sociedad = models.CharField(max_length=30,)
    nombre = models.CharField(max_length=30,)
    apellido = models.CharField(max_length=30,)
    edad = models.PositiveIntegerField()
    mail = models.EmailField(verbose_name='email', max_length=50)
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Sociedad: {self.sociedad}, E-mail: {self.mail}"
    

class Impuestos(models.Model):
    asesoramientofiscal = models.CharField(max_length=30,)
    nombre = models.CharField(max_length=30,)
    apellido = models.CharField(max_length=30,)
    edad = models.PositiveIntegerField()
    mail = models.EmailField(verbose_name='email', max_length=50)
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Asesoramiento Fiscal: {self.asesoramientofiscal}, E-mail: {self.mail}"

