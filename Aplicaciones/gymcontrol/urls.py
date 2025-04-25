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
    path('eliminar_cliente/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('suscripciones/', views.suscripciones, name='suscripciones'),
    path('nueva_suscripcion/', views.nueva_suscripcion, name='nueva_suscripcion'),
    path('guardar_suscripcion/', views.guardar_suscripcion, name='guardar_suscripcion'),
    path('eliminar_suscripcion/<int:id>/', views.eliminar_suscripcion, name='eliminar_suscripcion'),
    
    path('registrar_abono/<int:suscripcion_id>/', views.registrar_abono, name='registrar_abono'),
    path('abonos/', views.abonos, name='abonos'),
    path('eliminar_abono/<int:abono_id>/', views.eliminar_abono, name='eliminar_abono'),
    
    path('notificaciones/', views.notificaciones, name='notificaciones'),
    path('noti/<int:pk>/leida/', views.marcar_leida, name='marcar_leida'),
    path('noti/todas/leidas/', views.marcar_todas_leidas, name='marcar_todas_leidas'),


]