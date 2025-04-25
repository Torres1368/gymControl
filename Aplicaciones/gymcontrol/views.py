from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from decimal import Decimal
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from datetime import date
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Cliente, TipoPago, Suscripcion
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

def salir(request):
    logout(request)
    return redirect('/')

    
#Informacion del usuario
@login_required
def perfil_usuario(request):
    user = request.user

    # Obtener o crear el perfil si no existe
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        if 'imagen' in request.FILES:
            profile.imagen = request.FILES['imagen']
            profile.save()
            messages.success(request, 'Foto de perfil actualizada correctamente.')
            return redirect('perfil_usuario')  # Asegúrate que este sea tu URL name

    return render(request, 'perfil/perfil.html', {
        'user': user,
        'profile': profile
    })

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def notificaciones(request):
    # Obtener todas las notificaciones (leídas y no leídas)
    todas_notificaciones = Notificacion.objects.all().order_by('-fecha')
    return render(request, 'notificacion/notificacion.html', {'todas_notificaciones': todas_notificaciones, 'navbar': 'notificaciones'})


def marcar_leida(request, pk):
    n = get_object_or_404(Notificacion, pk=pk)
    n.leida = True
    n.save()
    return redirect(request.META.get('HTTP_REFERER', 'index'))

def marcar_todas_leidas(request):
    Notificacion.objects.filter(leida=False).update(leida=True)
    return redirect(request.META.get('HTTP_REFERER', 'index'))

@login_required
def clientes(request):
    clientes=Cliente.objects.all()
    return render(request,'cliente/cliente.html',{'clientes':clientes ,'navbar': 'clientes'})

@login_required
def nuevo_cliente(request):
    return render(request,'cliente/nuevo_cliente.html')

@login_required
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

@login_required
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


@login_required
def eliminar_cliente(request, id):
    clienteEliminar = get_object_or_404(Cliente, id=id)
    try:
        clienteEliminar.delete()
        messages.success(request, 'Cliente eliminado exitosamente')
    except ProtectedError:
        messages.error(request, 'No se puede eliminar este cliente porque está relacionado con otros registros.')
    return redirect('/clientes')

@login_required
def suscripciones(request):
    clientes=Cliente.objects.all()
    suscripciones = Suscripcion.objects.all()
    return render(request,'suscripcion/suscripcion.html',{'clientes':clientes ,'suscripciones':suscripciones, 'navbar': 'suscripciones'})

@login_required
def nueva_suscripcion(request):
    clientes=Cliente.objects.all()
    tiposPagos=TipoPago.objects.all()
    return render(request,'suscripcion/nueva_suscripcion.html',{'clientes':clientes, 'tiposPagos':tiposPagos})



@login_required
def guardar_suscripcion(request):
    if request.method == 'POST':
        cliente_id    = request.POST["cliente"]
        tipo_pago_id  = request.POST["tipo_pago"]
        fecha_inicio  = request.POST.get("fecha_inicio")
        fecha_fin     = request.POST.get("fecha_fin")
        pago_inicial  = request.POST["pago_inicial"].replace(",", ".")
        total_pagar   = request.POST["total_pagar"].replace(",", ".")
        estado        = request.POST["estado"]

        cliente = Cliente.objects.get(id=cliente_id)
        pendiente = Suscripcion.objects.filter(
            cliente=cliente,
            estado='pendiente'
        ).exists()
        if pendiente:
            messages.error(
                request,
                'No se puede crear la suscripción: el cliente tiene un pago pendiente.'
            )
            # Puedes redirigir a la lista de suscripciones
            return redirect('/nueva_suscripcion')
            # o volver a renderizar el formulario con los datos


        # Si no hay pendiente, seguimos con la creación
        tipo_pago = TipoPago.objects.get(id=tipo_pago_id)
        Suscripcion.objects.create(
            cliente=cliente,
            tipo_pago=tipo_pago,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            pago_inicial=pago_inicial,
            total_pagar=total_pagar,
            estado=estado
        )
        messages.success(request, 'Suscripción guardada exitosamente')
        return redirect('/suscripciones')

    # Si no es POST, mostrar tu formulario (opcional)
    return render(request, 'suscripciones/form.html', {
        'clientes': Cliente.objects.all(),
        'tipos_pago': TipoPago.objects.all()
    })


@login_required
def eliminar_suscripcion(request, id):
    suscripcionEliminar = get_object_or_404(Suscripcion, id=id)
    try:
        suscripcionEliminar.delete()
        messages.success(request, 'Suscripción eliminada exitosamente')
    except ProtectedError:
        messages.error(request, 'No se puede eliminar esta suscripción porque está relacionada con otros registros.')
    return redirect('/suscripciones') 

@login_required
def registrar_abono(request, suscripcion_id):
    # Obtén la suscripción correspondiente
    suscripcion = Suscripcion.objects.get(id=suscripcion_id)
    
    # Obtén el monto abonado y la fecha del formulario
    monto_abonado = request.POST.get('monto_abonado').replace(",", ".")
    fecha_abono = request.POST.get('fecha')
    
    # Convertir el monto abonado a decimal
    monto_abonado = Decimal(monto_abonado)
    
    # Registrar el abono en la base de datos
    abono = Abono(
        suscripcion=suscripcion,
        monto_abonado=monto_abonado,
        fecha=fecha_abono
    )
    abono.save()

    # Actualizar el total a pagar en la suscripción
    suscripcion.total_pagar -= monto_abonado  # Ya ambos son Decimal

    # Verificar si el total a pagar es 0 o menor y actualizar el estado
    if suscripcion.total_pagar <= 0:
        suscripcion.estado = 'activa'
    else:
        suscripcion.estado = 'pendiente'

    # Guardar los cambios en la suscripción
    suscripcion.full_clean() # Llamar al método clean para validar los campos del choice estado
    suscripcion.save()

    # Redirigir o devolver una respuesta
    messages.success(request, 'El abono ha sido registrado exitosamente')    
    return redirect('/suscripciones')  # Puedes redirigir a cualquier vista que necesites 

@login_required
def abonos(request):
    abonos = Abono.objects.select_related('suscripcion').all()
    return render(request, 'abono/abono.html', {
        'abonos': abonos,
        'navbar': 'abonos'
    })
   
@login_required    
def eliminar_abono(request, abono_id):
    abono = get_object_or_404(Abono, id=abono_id)
    suscripcion = abono.suscripcion

    # Sumar el abono eliminado al total_pagar
    suscripcion.total_pagar += abono.monto_abonado

    # Cambiar el estado si queda saldo pendiente
    if suscripcion.total_pagar > 0:
        suscripcion.estado = 'pendiente'

    suscripcion.save()
    abono.delete()

    messages.success(request, 'Abono eliminado exitosamente')
    return redirect('/abonos')  # Cambia esta ruta si tu vista o template es diferente