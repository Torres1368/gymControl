from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
    path('guardar_cliente/', views.guardar_cliente, name='guardar_cliente'),
    path('editar_cliente/<id>', views.editar_cliente, name='editar_cliente'),
    path('procesarinformacionCliente/', views.procesarinformacionCliente),
    path('eliminar_cliente/<id>', views.eliminar_cliente, name='eliminar_cliente'),

]