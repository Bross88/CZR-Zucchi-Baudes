from django.urls import path
from AppFinal.views import *

urlpatterns = [
    
    path('', inicio, name='AppFinalInicio'),
    path('monotributista/', monotributista, name='AppFinalMonotributista'),
    path('responsableinscripto/', responsable_inscripto, name='AppFinalResponsable'),
    path('impuesto/', impuestos, name='AppFinalImpuesto'),
    path('formulario/', formulario, name='AppFinalFormulario'),
    path('busqueda_nombre/', busqueda_nombre, name='AppFinalBusquedaNombre'),
    path('busqueda_nombre_post/', busqueda_nombre_post, name='AppFinalBusquedaNombrePost'),
    # path('eliminar_nombre/', eliminar_nombre, name='AppFinalEliminarNombre'),
    # path('editar_nombre/', editar_nombre, name='AppFinalEditarNombre'),
    path('nosotros/', sobre_nosotros, name='AppFinalnosotros'),
    path('profile/',profile, name='AppFinalprofile'),
    path('about/', about, name='AppFinalabout'),
    path('mapa/',mapa_interactivo, name='AppFinalmapainteractivo'),

]