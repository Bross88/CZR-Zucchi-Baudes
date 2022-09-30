from django.db import models


categoria_monotributista = [
    (1, 'Categoria A'),
    (2, 'Categoria B'),
    (3, 'Categoria C'),
    (4, 'Categoria D')
   ]

actividad_monotributista = [
    (1, 'Transpote de cargas N.C.P'),
    (2, 'Servicios Inmobiliarios'),
    (3, 'Enseñanza'),
    (4, 'Construccion'),
    (5, 'Maestranza'),
    (6, 'Servicio Postal'),
    (7, 'Categoria D'),
    (8, 'Edición n.c.p'),
    (9, 'Venta al por menor'),
    (10, 'Venta al por mayor'),
    (11, 'Servicios de consultores en tecnología'),
    (12, 'Arrendamiento financiero'),
    (13, 'Obras Sociales'),
    (14, 'Administración de fondos de pensiones'),
    (15, 'Servicios de bolsas de comercio'),
    (16, 'Servicios de administración de consorcios de edificios'),
    (17, 'Servicios de gerenciamiento de empresas'),
    (18, 'Servicios de arquitectura e ingeniería'),
    (19, 'Alquiler de vehículos automotores n.c.p'),
    (20, 'Compra-venta')
   ]


class Monotributista(models.Model):
    categoria = models.CharField(
        max_length=30,
        null=False, 
        blank=False,
        choices=categoria_monotributista
    )
    actividad =models.CharField(
        max_length=250,
        null=False,
        blank=False,
        choices=actividad_monotributista
    )

    
    

class ResponsableInscripto(models.Model):
    pass
    
    
    

class Impuestos(models.Model):
    pass
    
    
    

