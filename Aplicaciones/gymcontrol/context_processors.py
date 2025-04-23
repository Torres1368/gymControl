from datetime import date
from .models import Suscripcion

def notificaciones_context(request):
    suscripciones_vencidas = Suscripcion.objects.filter(fecha_fin__lt=date.today())
    notificaciones = []

    for s in suscripciones_vencidas:
        notificaciones.append({
            'cliente': f"{s.cliente.nombre} {s.cliente.apellido}",
            'mensaje': f"La suscripción de {s.cliente.nombre} {s.cliente.apellido} ha vencido",
            'fecha': s.fecha_fin,
        })

    return {'notificaciones': notificaciones}
