from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_request,name='UserApplogin'),
    path('registro/',indexreg, name='UserAppregister'),
    #path('editar',editar_usuario, name='UserAppeditar'),
    path('pagina_dos/', pagina_dos, name='UserAppPaginaDos'),
]
  