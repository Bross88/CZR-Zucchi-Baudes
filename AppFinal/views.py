import email
from django.shortcuts import render, redirect
from http.client import HTTPResponse
from mailbox import NoSuchMailboxError
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from AppFinal.forms import Categorias,CategoriasResponsableInscripto,CategoriasImpuestos,CategoriasInversiones #,Formulario,BusquedaNombreFormulario



def mapa_interactivo(request):
    
    return render(request, 'AppFinal/map.html')


def profile(request):
    
    return render(request, 'AppFinal/profile.html')

def inicio(request):
    
    return render(request, 'Index.html')

def about(request):
    
    return render(request, 'AppFinal/about.html')

def sobre_nosotros(request):
    
    return render(request, 'AppFinal/sobre_nosotros.html')

#________________MONOTRIBUTISTA VIEW select_________________________________________
def monotributista(request):

    contexto = {
        
        'form': Categorias(),
    
    }
    
    return render(request, 'AppFinal/monotributista.html', contexto)



#________________R I VIEW_________________________________________
def responsable_inscripto(request):
    
    contexto = {
        
        'form': CategoriasResponsableInscripto(),
    
    }
    
    return render(request, 'AppFinal/responsableinscripto.html', contexto)




#_______________IMPUESTOS VIEW_________________________________________
def impuestos(request):
    
    contexto = {
        
        'form': CategoriasImpuestos(),
    
    }
    
    return render(request, 'AppFinal/impuesto.html', contexto)


#_______________Inversiones VIEW_________________________________________

def inversiones(request):
        
    contexto = {
        
        'form': CategoriasInversiones(),
     
    }
    
    return render(request, 'AppFinal/inversiones.html', contexto)






#___________________________________________________________________________________________
"""
def formulario(request):
    
    if request.method == 'POST':
        miFormulario = Formulario(request.POST)
        
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            
            formulario1 = Monotributista(nombre=data.get('nombre'), apellido=data.get('apellido'),edad=data.get('edad'),mail=data.get('mail'))
            formulario1.save()
            
            return redirect('AppFinalFormulario')
        
    monotributistas = Monotributista.objects.all()
    
    contexto = {
        
        'form':Formulario(),
        'monotributistas':monotributistas
       
    }
    
    return render (request, 'AppFinal/formulario.html', contexto)


def busqueda_nombre(request):
    
    contexto = {
        
        'form': BusquedaNombreFormulario(),
    
    }
    
    return render(request, 'AppFinal/busqueda_nombre.html', contexto)


def busqueda_nombre_post(request):
    
    nombre = request.GET.get('nombre')
    
    monotributistas = Monotributista.objects.filter(nombre__icontains=nombre)
    
    contexto = {
        
        'monotributistas': monotributistas    
        }
    
    return render (request, 'AppFinal/formulario_filtrado.html', contexto)
"""



































# def eliminar_nombre(request,nombre):
#     eliminar_nombre = Monotributista.objects.get(nombre=nombre)
#     eliminar_nombre.delete()
    
#     messages.info(request, f"El nombre {eliminar_nombre} fue eliminado")
    
#     return redirect("AppFinalMonotributista")


# def editar_nombre(request, nombre):
#     editar_nombre = Monotributista.objects.get(nombre=nombre)
    
#     if request.method == 'POST':
#         miFormulario = Formulario(request.POST)
        
#         if miFormulario.is_valid():
            
#             data = miFormulario.cleaned_data
            
#             editar_nombre.nombre = data.get('nombre')
#             editar_nombre.apellido = data.get('apellido')
#             editar_nombre.edad = data.get('edad')
#             editar_nombre.mail = data.get('mail')
            
#             editar_nombre.save()
            
#             return redirect('AppFinalFormulario')
    
    
    
#     contexto = {
#         'form': Formulario(
#             initial={
#             "nombre": editar_nombre.nombre,
#             "apellido": editar_nombre.appelido,
            
#             } 
#         )  
#     }
    
#     return render (request, 'AppFinal/formulario.html', contexto)

