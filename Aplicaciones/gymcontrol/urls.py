from django.urls import path
from .import views

urlpatterns = [
    path('',views.user_login, name='user_login'),
    path('salir/',views.salir, name='salir'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('index/', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
    path('guardar_cliente/', views.guardar_cliente, name='guardar_cliente'),
    path('editar_cliente/<id>', views.editar_cliente, name='editar_cliente'),
    path('procesarinformacionCliente/', views.procesarinformacionCliente),
    path('eliminar_cliente/<id>', views.eliminar_cliente, name='eliminar_cliente'),
    path('suscripciones/', views.suscripciones, name='suscripciones'),
    path('nueva_suscripcion/', views.nueva_suscripcion, name='nueva_suscripcion'),
    path('guardar_suscripcion/', views.guardar_suscripcion, name='guardar_suscripcion'),
    path('editar_suscripcion/<id>', views.editar_suscripcion, name='editar_suscripcion'),
    path('procesarinformacionSuscripcion/', views.procesarinformacionSuscripcion),
    path('eliminar_suscripcion/<id>', views.eliminar_suscripcion, name='eliminar_suscripcion'),
    
    path('registrar_abono/<int:suscripcion_id>/', views.registrar_abono, name='registrar_abono'),
    path('abonos/', views.abonos, name='abonos'),


]