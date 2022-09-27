from django.urls import path
from .views import login_request,indexreg,pagina_dos,upload_avatar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',login_request,name='UserApplogin'),
    path('registro/',indexreg, name='UserAppregister'),
    #path('editar',editar_usuario, name='UserAppeditar'),
    path('pagina_dos/', pagina_dos, name='UserAppPaginaDos'),
    path('logout/',LogoutView.as_view(template_name='UserApp/Logout.html'), name='UserApplogout'),
    path('avatar/', upload_avatar, name='UserAppAvatar'),
]