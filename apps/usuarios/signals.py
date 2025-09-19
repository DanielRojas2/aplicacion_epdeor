from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from django.utils.timezone import now
from .models.PerfilUsuario import PerfilUsuario

@receiver(pre_save, sender=PerfilUsuario)
def actualizar_estado_usuario(sender, instance, **kwargs):
    hoy = now().date()
    if instance.baja and instance.baja < hoy:
        instance.estado = False
    else:
        instance.estado = True


@receiver(post_save, sender=PerfilUsuario)
def crear_usuario_actualizar_usuario(sender, instance, created, **kwargs):
    user = instance.usuario

    if created and not user:
        username = f"{instance.nombre}{instance.apellido_paterno}".lower()
        password = f"{instance.ci}.epdeor"

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=instance.nombre,
            last_name=instance.apellido_paterno,
        )

        instance.usuario = user
        instance.save(update_fields=['usuario'])

    elif user:
        user.is_active = instance.estado
        user.first_name = instance.nombre
        user.last_name = instance.apellido_paterno
        user.save()

    # ---- Lógica de roles ----
    UNIDAD_A_GRUPO = {
        "Activos Fijos y Almacenes": "Encargado de almacenes",
        "Sistemas Informáticos y Redes": "Encargado de sistemas",
        "Archivos y Ujier": "Encargado de archivos",
    }

    if instance.usuario:
        solicitante_group, _ = Group.objects.get_or_create(name="Solicitante")
        grupos = [solicitante_group]

        unidad = instance.puesto.unidad.unidad if instance.puesto and instance.puesto.unidad else None
        if unidad in UNIDAD_A_GRUPO:
            grupo_encargado, _ = Group.objects.get_or_create(name=UNIDAD_A_GRUPO[unidad])
            grupos.append(grupo_encargado)

        instance.usuario.groups.set(grupos)
