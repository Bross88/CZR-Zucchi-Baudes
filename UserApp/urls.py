from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_request,name='UserApplogin'),
    path('registro/',indexreg, name='UserAppregister'),
]
 