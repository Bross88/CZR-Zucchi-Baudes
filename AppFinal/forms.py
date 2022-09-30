from django import forms
from. models import Monotributista

class Formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    mail = forms.EmailField(max_length=50)

class BusquedaNombreFormulario(forms.Form):
    nombre = forms.CharField()


class Categorias(forms.ModelForm):
    class Meta:
        model= Monotributista
        fields = ['categoria','actividad']

    