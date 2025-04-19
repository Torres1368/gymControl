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
        fecha_nacimiento=request.POST.get("fecha_nacimiento") or None
        foto=request.FILES.get("foto")
                
        cliente=Cliente.objects.create(nombre=nombre,apellido=apellido,genero=genero,
                                       telefono=telefono,email=email,direccion=direccion,
                                       fecha_nacimiento=fecha_nacimiento,foto=foto)
    
        messages.success(request, 'Cliente guardado exitosamente')
        return redirect('/clientes')

def editar_cliente(request, id):
    cliente=Cliente.objects.get(id=id)
    return render(request, 'cliente/editar_cliente.html', {'cliente': cliente})

def procesarinformacionCliente(request):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    apellido=request.POST["apellido"]
    telefono=request.POST["telefono"]
    genero= request.POST["genero"]
    email=request.POST["email"]
    direccion=request.POST["direccion"]
    fecha_nacimiento=request.POST.get("fecha_nacimiento") or None
    nueva_foto=request.FILES.get("nueva_foto")
    clienteEditar=Cliente.objects.get(id=id)
    clienteEditar.nombre=nombre
    clienteEditar.apellido=apellido
    clienteEditar.telefono=telefono
    clienteEditar.genero=genero
    clienteEditar.email=email
    clienteEditar.direccion=direccion
    clienteEditar.fecha_nacimiento=fecha_nacimiento
    clienteEditar.foto=nueva_foto
    clienteEditar.save()
    messages.success(request, 'Los datos del cliente se han actualizado')    
    return redirect('/clientes')



def eliminar_cliente(request,id):
    clienteEliminar=Cliente.objects.get(id=id)
    clienteEliminar.delete()
    messages.success(request, 'Cliente eliminado exitosamente')
    return redirect('/clientes')

def suscripciones(request):
    clientes=Cliente.objects.all()
    suscripciones = Suscripcion.objects.all()
    return render(request,'suscripcion/suscripcion.html',{'clientes':clientes ,'suscripciones':suscripciones, 'navbar': 'suscripciones'})

def nueva_suscripcion(request):
    clientes=Cliente.objects.all()
    tiposPagos=TipoPago.objects.all()
    return render(request,'suscripcion/nueva_suscripcion.html',{'clientes':clientes, 'tiposPagos':tiposPagos})


def guardar_suscripcion(request):
    if request.method == 'POST':
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        telefono=request.POST["telefono"]
        genero= request.POST["genero"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        fecha_nacimiento=request.POST.get("fecha_nacimiento") or None
        foto=request.FILES.get("foto")
                
        cliente=Cliente.objects.create(nombre=nombre,apellido=apellido,genero=genero,
                                       telefono=telefono,email=email,direccion=direccion,
                                       fecha_nacimiento=fecha_nacimiento,foto=foto)
    
        messages.success(request, 'Cliente guardado exitosamente')
        return redirect('/clientes')

def editar_suscripcion(request, id):
    suscripciones=Suscripcion.objects.get(id=id)
    return render(request, 'suscripcion-/editar_suscripcion.html', {'suscripciones': suscripciones})

def procesarinformacionSuscripcion(request):
    return redirect('/clientes')



def eliminar_suscripcion(request,id):
    suscripcionEliminar=Suscripcion.objects.get(id=id)
    suscripcionEliminar.delete()
    messages.success(request, 'Cliente eliminado exitosamente')
    return redirect('/suscripciones')

