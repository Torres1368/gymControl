from Aplicaciones.gymcontrol.models import Notificacion

def generar_notificacion(suscripcion):
    cliente = suscripcion.cliente
    mensaje = f"La suscripción de {cliente.nombre} {cliente.apellido} ha vencido"
    
    # Evita duplicados del mismo mensaje y cliente
    if not Notificacion.objects.filter(mensaje=mensaje, cliente=cliente).exists():
        Notificacion.objects.create(mensaje=mensaje, cliente=cliente)
