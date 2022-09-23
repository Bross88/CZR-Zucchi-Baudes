from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Avatar, Register


#-------------------------------------------------------------------------------------------------------

class Registerform(forms.ModelForm):   
    class Meta:
        model=Register
        fields= "__all__"


class AvatarForm(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = "__all__"