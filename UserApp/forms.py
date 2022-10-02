from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Avatar


#--------------registro2-----------------------------------------------------------------------------------------
"""
class Registerform(forms.ModelForm):   
    class Meta:
        model=Register
        fields= "__all__"

"""
#_______________________________REGISTRO________________________________________________________________________

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField(max_length=150)
    

    class Meta:
        model=User
        fields= ('username','last_name', 'email')


#_____________________________editar usuario perfil___________________________________________
class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    last_name = forms.CharField(label='apellido',max_length=50)
    username= forms.CharField(label='nombre',max_length=50)
    

    class Meta:
        model=User
        fields= ('username','last_name', 'email')




#___________________________________________AVATAR__________________________________________
class AvatarForm(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = "__all__"
