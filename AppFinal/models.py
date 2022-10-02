from django.db import models

#______________________________MONOTRIBUTISTAS____________________________________
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
        max_length=100,
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

    
#_______________________________RESPONSABLES INSCRIPTOS______________________________________________
   
categoria_RI = [
    (1, 'IVA Responsable Inscripto'),
    (2, 'IVA Responsable no Inscripto'),
    (3, 'IVA no Responsable'),
    (4, 'IVA Sujeto Exento'),
    (5, 'Consumidor Final'),
    (6, 'Responsable Monotributo'),
    (7, 'Sujeto no Categorizado'),
    (8, 'Proveedor del Exterior'),
    (9, 'Cliente del Exterior'),
    (10, 'IVA Liberado Ley Nº 19.640'),
    (11, 'IVA Responsable Inscripto Agente de Percepción'),
    (12, 'Pequeño Contribuyente Eventual'),
    (13, 'Monotributista Social'),
    (14, 'Pequeño Contribuyente Eventual Social')
    ]


actividad_responsableinscripto = [
    (1, 'Trabajador Autonomo'),
    (2, 'Empleador'),
    ]


class ResponsableInscripto(models.Model):
    categoria = models.CharField(
        max_length=100,
        null=False, 
        blank=False,
        choices=categoria_RI
    )

    actividad =models.CharField(
        max_length=250,
        null=False,
        blank=False,
        choices=actividad_responsableinscripto
    
    )
    
    
    

#___________________________________IMPUESTOS__________________________________________
categoria_impuestos = [
    (1, 'Ganancia de primera categoría: '),
    (2, 'Ganancia de seguda categoría: '),
    (3, 'Ganancia de tercera categoría: '),
    (4, 'Ganancia de cuarta categoría: '),
    ]


actividad_impuestos = [
    (1, 'Inmuebles Urbanos y Rurales'),
    (2, 'Acciones'),
    (3, 'Intereses'),
    (4, 'Dividendos'),
    (5, 'Sociedades'),
    (6, 'Empresas Unipersonales'),
    (7, 'Trabajo Personal')
    ]


class Impuestos(models.Model):
    categoria = models.CharField(
        max_length=100,
        null=False, 
        blank=False,
        choices=categoria_impuestos
    )
    actividad =models.CharField(
        max_length=250,
        null=False,
        blank=False,
        choices=actividad_impuestos
    
    
    )
    #_______________________________INVERSIONES______________________________________
Categoria_Inversiones = [
    (1, 'Plazos Fijos '),
    (2, 'Inversion en la Bolsa '),
    (3, 'Bots de Minado Pasivo '),
    (4, 'Criptomonedas '),
    (4, 'Exchange'),

    ]

Monto_Inversiones = [
    (1, 'Monto de inversion 1000'),
    (2, 'Monto de inversion 5000'),
    (3, 'Monto de inversion 10000'),
    (4, 'Monto de inversion 30000'),
    (5, 'Monto de inversion 50000'),
    (6, 'Monto de inversion 100000'),
    (7, 'Monto de inversion 500000'),
    (7, 'Otro Monto/Other Amount')
    ]
Tipo_Moneda = [
    (1, 'ARS'),
    (2, 'USD'),
    (3, 'EURO'),
    (4, 'BRL'),
    (5, 'AED'),
    (6, 'UYU'),
    (7, 'RUB'),
    (7, 'BSD'),
    (7, 'CLP'),
    (7, 'CNY'),
    (7, 'COP'),
    (7, 'RUB'),
    (7, 'MXN'),
    (7, 'GBP'),
    (7, 'Otra moneda/Other Currency')
    ]

class Inversiones(models.Model):
    modo = models.CharField(
        max_length=100,
        null=False, 
        blank=False,
        choices=Categoria_Inversiones 
    )
    monto =models.CharField(
        max_length=250,
        null=False,
        blank=False,
        choices=Monto_Inversiones
    
    )
    moneda =models.CharField(
        max_length=250,
        null=False,
        blank=False,
        choices=Tipo_Moneda
        
    )

