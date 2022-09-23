from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',login_request,name='UserApplogin'),
    path('registro/',indexreg, name='UserAppregister'),
    path('logout/',LogoutView.as_view(template_name='UserApp/Logout.html'), name='UserApplogout'),
    path('avatar/', upload_avatar, name='UserAppAvatar'),
]
 