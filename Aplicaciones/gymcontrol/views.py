from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate, login
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            # Este bloque es para el la img perfil L
            # Este bloque es para la imagen de perfil
            try:
                profile = Profile.objects.get(user=user)
                request.session['imagen'] = profile.imagen.url if profile.imagen else None
            except Profile.DoesNotExist:
                request.session['imagen'] = None
            # End --- eliminar si llega a ser inecesario

            return redirect('/clientes')  # Redirige a la página principal después del login
        else:
            # Si las credenciales son incorrectas
            messages.error(request, 'Credenciales incorrectas')
            return render(request, 'registration/login.html')
        

    return render(request, 'registration/login.html')

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
        cliente_id = request.POST["cliente"]
        tipo_pago_id = request.POST["tipo_pago"]
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_fin = request.POST.get("fecha_fin")
        pago_inicial = request.POST["pago_inicial"]
        total_pagar = request.POST["total_pagar"]
        estado=request.POST["estado"]
        
        cliente=Cliente.objects.get(id=cliente_id)
        tipo_pago=TipoPago.objects.get(id=tipo_pago_id)
        suscripcion=Suscripcion.objects.create(cliente=cliente,tipo_pago=tipo_pago,fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,pago_inicial=pago_inicial,total_pagar=total_pagar,estado=estado)
        messages.success(request, 'Suscripcion guardada exitosamente')
        return redirect('/suscripciones')
    

def editar_suscripcion(request, id):
    suscripciones=Suscripcion.objects.get(id=id)
    clientes=Cliente.objects.all()
    tiposPagos=TipoPago.objects.all()
        

    
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

