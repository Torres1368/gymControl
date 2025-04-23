from datetime import date
from django.core.cache import cache
from .models import Suscripcion

class ExpirarUnaVezAlDiaMiddleware:
    """
    Cada petición comprueba si ya expiramos suscripciones hoy.
    Si no, marca como 'vencida' las suscripciones activas
    cuya fecha_fin < hoy, y guarda en cache la fecha de hoy.
    """

    CACHE_KEY = 'suscripciones_expiradas_hasta'

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Obtenemos la fecha de hoy sin tocar timezone.localdate()
        hoy = date.today()
        ultima = cache.get(self.CACHE_KEY)

        # Si no hemos corrido hoy la expiración, la ejecutamos una vez
        if ultima != str(hoy):
            Suscripcion.objects.filter(
                estado='activa',
                fecha_fin__lt=hoy
            ).update(estado='vencida')
            # Marcamos en cache que ya expiramos para no repetirlo el mismo día
            cache.set(self.CACHE_KEY, str(hoy), None)

        return self.get_response(request)
