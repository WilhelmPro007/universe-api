from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    karma = models.IntegerField(default=0)
    is_online = models.BooleanField(default=False)
    last_active = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal para crear automáticamente un perfil de usuario cuando se crea un nuevo usuario.
    """
    if created:
        profile = UserProfile.objects.create(user=instance)
        # Asignar grupo por defecto
        user_group = Group.objects.get_or_create(name='User')[0]
        instance.groups.add(user_group)
        # Si es superusuario, asignar grupo de administrador
        if instance.is_superuser:
            admin_group = Group.objects.get_or_create(name='Administrator')[0]
            instance.groups.add(admin_group)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal para guardar el perfil de usuario cuando se actualiza el usuario.
    """
    instance.profile.save()
