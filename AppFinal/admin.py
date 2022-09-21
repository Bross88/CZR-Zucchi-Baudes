from django.contrib import admin
from AppFinal.models import *

class MonotributistaAdmin(admin.ModelAdmin):
    # list_display=("nombre","apellido","mail")
    search_fields=("nombre", "apellido", "mail")
    list_filter=("categoria","nombre", "apellido", "mail",)
    
    
class ResponsableInscriptoAdmin(admin.ModelAdmin):
    # list_display=("nombre","apellido","mail")
    search_fields=("nombre", "apellido", "mail")
    list_filter=("sociedad","nombre", "apellido", "mail",)
    
    
class ImpuestosAdmin(admin.ModelAdmin):
    # list_display=("nombre","apellido","mail")
    search_fields=("nombre", "apellido", "mail")
    list_filter=("asesoramientofiscal","nombre", "apellido", "mail",)


admin.site.register(Monotributista, MonotributistaAdmin)
admin.site.register(ResponsableInscripto, ResponsableInscriptoAdmin)
admin.site.register(Impuestos, ImpuestosAdmin)