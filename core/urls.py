from django.contrib import admin
from django.urls import path
from reservacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('clientes/', views.clientes, name='clientes'),
    path('crear/reservacion/', views.reservacion, name='reservacion'),
    path('clientes/registrar_clientes/', views.registrar_clientes, name='registrar_clientes'),
    path('logout/', views.cerrar_sesion, name='logout' ),
    path('signin/', views.signin, name='signin'),
]
