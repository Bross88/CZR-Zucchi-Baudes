from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login #PasswordChangeForm 
#from .models import Register
#from .forms import *
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,AvatarForm,Avatar
from django.contrib.auth.models import User
#from django.views.generic import FormView        perfil password change
#from django.urls import reverse_lazy             perfil password change

#__________________________________________________________________________________________________________________________


#___________________vista p2__________________________________________________________________________________
@login_required
def pagina_dos(request):
    return render(request, 'UserAppTemplate/pagina_dos.html')


#_________________________LOGIN_____________________________________________________________________________________

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
                

                return redirect('UserAppPaginaDos')
                
            else:
                messages.info(request, 'Error, verifique Usuario o Contraseña')
                
        else:
            messages.info(request, 'Inicio de sesion erroneo, por favor verifique su usuario y contraseña')
            
        return redirect('AppFinalInicio')

    contexto = {
        'form': AuthenticationForm(),
        
    }
    return render(request, 'UserAppTemplate/login.html', contexto)
 


#________________________________REGISTRO2____________________________________________________________________________
"""
def indexreg(request):
        contexto = {}
        
        if request.method == 'POST':
            form=Registerform(request.POST)

            if form.is_valid():
                nombre=form.cleaned_data.get('nombre')
                apellido=form.cleaned_data.get('apellido')
                telefono_movil=form.cleaned_data.get('telefono_movil')
                pais=form.cleaned_data.get('pais')
                email=form.cleaned_data.get('email')
                cuit=form.cleaned_data.get('cuit')
                password=form.cleaned_data.get('password')

                reg = Register(
                    nombre=nombre,
                    apellido=apellido,
                    telefono_movil=telefono_movil, 
                    pais=pais,  
                    email=email,   
                    cuit=cuit,
                    password=password,
                )
                reg.save()

                return redirect('AppFinalInicio')

        else:
            form = Registerform()
            contexto= {
                'form' : form
            }

        return render(request,'UserAppTemplate/login_reg.html',contexto)

"""
 #_________________________________ENVIO DE MAIL________________________________________________________

def enviar_email(mail):

    contexto = {'mail' : mail}
    
    template = get_template('correo.html')   # o sera appfinalinicio?
    content = template.render(contexto)

    email = EmailMultiAlternatives(
        'Correo de prueba',
        settings.EMAIL_HOST_USER, # quien envia el mail (settings)
        [mail],# destinatario
       # cc=                     # enviar copia a X persona
    )


    email.attach_alternative(contexto, 'text/html')
    email.send()



def index_email(request):
    if request.method == 'POST':    
        mail= request.POST.get('mail')
        enviar_email(mail)
    return render(request, 'AppFinalInicio', {})



#_______________________________EDITAR USUARIO______________________________________________________________________
"""
@login_required
def editar_usuario(request):
    usuario=request.user
    if request.method == 'POST':
        form=Registerform(request.POST)
        if form.is_valid():
            
            data = form.cleaned_data()


            usuario.nombre = data.get('nombre')
            usuario.apellido = data.get('apellido')
            usuario.email = data.get('email')
           
            
            usuario.save()

    contexto ={
        'form': Registerform(
            initial = {
                'nombre':usuario.nombre,
                'apellido':usuario.apellido,
                'telefono_movil':usuario.telefono_movil,
                'pais':usuario.pais,
                'email':usuario.email,
                'cuit':usuario.cuit,
                
               
            }),
            'nombre_form': 'registro'
    }
    return render(request, 'Editar.html',contexto)

"""
#_______________________REGISTRO_____________________________________________________________________________________________


def indexreg(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            #Avatar= Avatar(user=user,imagen=form.cleaned.data.get('imagen'))
            #Avatar.save()

            messages.info(request,'Registro Satisfactorio')

        else:
            messages.info(request,'Error al Registrar')
        return redirect('AppFinalInicio')

    contexto= {
                'form' : UserRegisterForm(),
            }

    return render(request,'UserAppTemplate/login_reg.html',contexto)





#------------------------------Avatar---------------------------------------
def upload_avatar(request):
    if request.POST == "POST":
        
        formulario = AvatarForm(request.POST, request.FILES)
        
        if formulario.is_valid():
            
            data=formulario.cleanead_data
            avatar= Avatar.objects.filter(user=data.get("usuario"))
            
            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()
                 
            else:
                avatar= Avatar(user=data.get("user"), imagen=data.get("imagen"))
                avatar.save()
                
        return redirect("AppFinalInicio")
    
    contexto={
        "form":AvatarForm(),
        "Enviar": "Crear"    
    }
    
    return render(request, "UserApp/avatar.html", contexto)
    

#__________________________________________profile view_______________________________________________
def profile(request,username=None):
    current_user=request.user
    if username:
        user = User.objects.get(username=username)
        user = User.objects.get(email=user.email)
        user = User.objects.get(last_name=user.last_name)

    else:
        user=current_user
    return render(request, "UserApp/profile.html", {'user':user},{'email' : user.email},{'last_name',user.last_name})


#___________________________________________profile password_________________________________
"""
@login_required
class UserChangePasswordView(FormView):
    model = User
    form_class = PasswordChangeForm
    template_name = 'AppFinal/profile.html'
    success_url: reverse_lazy('login')

    def get_form(self, form_class=None):
        form =PasswordChangeForm(user=self.request.user)
        return form

"""



