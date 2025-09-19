from django.db import models
from django.contrib.auth.models import User
from .Puesto import Puesto

class PerfilUsuario(models.Model):
    nombre = models.CharField(max_length=25, blank=False, null=False)
    apellido_paterno = models.CharField(
        max_length=25, blank=False, null=False
    )
    apellido_materno = models.CharField(
        max_length=25, blank=False, null=False
    )
    alta = models.DateField(auto_now_add=True)
    baja = models.DateField()
    estado = models.BooleanField(default=True)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

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
