from dataclasses import dataclass
from email.errors import NoBoundaryInMultipartDefect
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Register
from .forms import *
from django.http import HttpResponseRedirect

#------------------------LOGIN----------------------------------------------------------------    

def login_request(request): 
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            data= form.cleaned_data
            
            usuario= data.get('username') # si no recibe info devuelve NONE por defecto evita crasheo
            contra= data.get('password')

            user= authenticate(username=usuario, password=contra) # sino trae la info devuelve NONE o User

            if user:  #vamos a verificar si hay usuario cargado
                login(request, user)
                messages.info(request, 'inicio de sesion valido')
                
            else:
                messages.info(request, 'Error, verifique Usuario o Contraseña')
                
        else:
            messages.info(request, 'inicio de sesion invalido')
            
        return redirect('AppFinalInicio')

    contexto = {
        'form': AuthenticationForm(),
        
    }
    return render(request, 'UserAppTemplate/login.html', contexto)

#---------------------------------------------------------------------------------------------------------------

    #-------registro---------------------------------------------------------------------------------------------------

def indexreg(request):
        contexto = {}
        
        if request.method == 'POST':
            form.RegisterForm(request.POST)

            if form.is_valid():
                nombre=form.cleaned_data.get('nombre')
                apellido=form.cleaned_data.get('apellido')
                telefono_movil=form.cleaned_data.get('telefono_movil')
                pais=form.cleaned_data.get('pais')
                email=form.cleaned_data.get('email')
                cuit=form.cleaned_data.get('cuit')
                #password=form.cleaned_data.get('password')

                reg = Register(
                    nombre=nombre,
                    apellido=apellido,
                    telefono_movil=telefono_movil,
                    pais=pais,  
                    email=email,   
                    cuit=cuit,
                    #password=password,
                )
                reg.save()

                return HttpResponseRedirect('/AppFinalInicio/')

        else:
            form = Registerform()
            contexto= {
                'form' : form
            }

        return render(request,'UserAppTemplate/login_reg.html',contexto)


 