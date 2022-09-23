import email
from django.shortcuts import render, redirect
from http.client import HTTPResponse
from mailbox import NoSuchMailboxError
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from AppFinal.forms import *
from AppFinal.models import Impuestos, Monotributista, ResponsableInscripto


def profile(request):
    
    return render(request, 'AppFinal/profile.html')

def inicio(request):
    
    return render(request, 'Index.html')

def about(request):
    
    return render(request, 'AppFinal/about.html')

def sobre_nosotros(request):
    
    return render(request, 'AppFinal/sobre_nosotros.html')


def monotributista(request): 
    
    monotributista1 = Monotributista(categoria="A", nombre="José", apellido="Hernandez", edad=55 , mail="josehernandez@gmail.com")
    monotributista1.save()
    
    #monotributistas = Monotributista.objects.all()[:3]
    
    contexto = {
        'monotributista1':monotributista1,
                  }
    return render(request, 'AppFinal/monotributista.html', contexto)


def responsable_inscripto(request):
    
    responsable_inscripto1 = ResponsableInscripto(sociedad="S.R.L.", nombre="Maria", apellido="Gomez", edad=44 , mail="mariagomez@gmail.com")
    responsable_inscripto1.save()
    
    #responsables = ResponsableInscripto.objects.all()[:3]
    
    contexto = {
        "responsable_inscripto1":responsable_inscripto1,
            }
    return render(request, 'AppFinal/responsableinscripto.html', contexto)


def impuestos(request):
    
    impuestos1 = Impuestos(asesoramientofiscal="I.V.A", nombre="Marcos", apellido="Fernandez", edad=65 , mail="marcosfernandez@gmail.com")
    impuestos1.save()
        
    #impuestos = Impuestos.objects.all()[:3]
    
    contexto = {
        "impuestos1":impuestos1,
            }
    return render(request, 'AppFinal/impuesto.html', contexto)


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

