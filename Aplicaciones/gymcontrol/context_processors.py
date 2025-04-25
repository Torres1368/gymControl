# gymcontrol/context_processors.py


from Aplicaciones.gymcontrol.models import Notificacion


def notificaciones_context(request):
    notis = Notificacion.objects.filter(leida=False).order_by('-fecha')[:5]
    return {'notificaciones': notis}
