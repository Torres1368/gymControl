from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def clientes(request):
    clientes=Cliente.objects.all()
    return render(request,'cliente/cliente.html',{'clientes':clientes ,'navbar': 'clientes'})

def nuevo_cliente(request):
    return render(request,'cliente/nuevo_cliente.html')

def guardar_cliente(request):
    if request.method == 'POST':
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        telefono=request.POST["telefono"]
        genero= request.POST["genero"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        fecha_nacimiento=request.POST["fecha_nacimiento"]
        foto=request.FILES.get("foto")
        cliente=Cliente.objects.create(nombre=nombre,apellido=apellido,genero=genero,
                                       telefono=telefono,email=email,direccion=direccion,
                                       fecha_nacimiento=fecha_nacimiento,foto=foto)
    
        messages.success(request, 'Cliente guardado exitosamente')
        return redirect('/clientes')

def editar_cliente(request, id):
    cliente=Cliente.objects.get(id=id)
    return render(request, 'cliente/editar_cliente.html', {'cliente': cliente})
