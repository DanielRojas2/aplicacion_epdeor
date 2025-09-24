import re
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .Puesto import Puesto

def validar_nombre_apellido(value):
    if not re.match(r'^[a-zA-Z\s]+$', value):
        raise ValidationError(f'El campo "{value}" solo puede contener letras y espacios.')
    
def validar_ci(value):
    if not re.match(r'^\d{7}$', value):
        raise ValidationError(f'El C.I. debe contener 7 dígitos.')
class PerfilUsuario(models.Model):
    nombre = models.CharField(
        max_length=25, blank=False, null=False,
        validators=[validar_nombre_apellido]
    )
    apellido_paterno = models.CharField(
        max_length=25, blank=False, null=False,
        validators=[validar_nombre_apellido]
    )
    apellido_materno = models.CharField(
        max_length=25, blank=False, null=False,
        validators=[validar_nombre_apellido]
    )
    ci = models.CharField(
        max_length=7, blank=False, null=False,
        validators=[validar_ci]
    )
    alta = models.DateField(auto_now_add=True)
    baja = models.DateField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuarios"

        constraints = [
            models.UniqueConstraint(
                fields=['nombre', 'apellido_paterno', 'apellido_materno'],
                name='unique_full_name'
            )
        ]
    
    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} | {self.usuario}"
