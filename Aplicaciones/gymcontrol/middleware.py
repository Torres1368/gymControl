# gymcontrol/middleware.py

from datetime import date
from django.core.cache import cache
from .models import Suscripcion
from .utils.notificaciones import generar_notificacion

class ExpirarYNotificarMiddleware:
    CACHE_KEY = 'suscripciones_expiradas_hasta'

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        hoy = date.today().isoformat()
        if cache.get(self.CACHE_KEY) != hoy:
            qs = Suscripcion.objects.filter(estado='activa', fecha_fin__lt=date.today())
            for sus in qs:
                generar_notificacion(sus)
            qs.update(estado='vencida')
            cache.set(self.CACHE_KEY, hoy, None)
        return self.get_response(request)
