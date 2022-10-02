from django import forms
from. models import Monotributista,ResponsableInscripto,Impuestos,Inversiones



#____________________________________________________________________________________

class Formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    mail = forms.EmailField(max_length=50)
#__________________________________________________________________________________
class BusquedaNombreFormulario(forms.Form):
    nombre = forms.CharField()

#__________________________________________________________________________________
class Categorias(forms.ModelForm):
    class Meta:
        model= Monotributista
        fields = ['categoria','actividad']
#__________________________________________________________________________________
class CategoriasResponsableInscripto(forms.ModelForm):
    class Meta:
        model= ResponsableInscripto
        fields = ['categoria','actividad']

#__________________________________________________________________________________
class CategoriasImpuestos(forms.ModelForm):
    class Meta:
        model= Impuestos
        fields = ['categoria','actividad']

#__________________________________________________________________________________
class CategoriasInversiones(forms.ModelForm):
    class Meta:
        model= Inversiones
        fields = ['modo','monto','moneda'] 