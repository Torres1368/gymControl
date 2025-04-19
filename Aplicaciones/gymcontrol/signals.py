from django.db.models.signals import post_save
from django.dispatch import receiver
#imports de signa profile
from django.contrib.auth.models import User
from .models import Profile  

#creacion de tabla profile imagenes al crear un usuario
@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    instance.profile.save()