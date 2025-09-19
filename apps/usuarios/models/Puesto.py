from django.db import models
from .Departamento import Departamento
from .Unidad import Unidad

class Puesto(models.Model):
    nro_item = models.CharField(
        primary_key=True,
        max_length=15,
        blank=False,
        null=False,
        unique=True
    )
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Puesto"
        verbose_name_plural = "Puestos"
        constraints = [
            models.UniqueConstraint(
                fields=['departamento', 'unidad'],
                name='unique_departamento_unidad'
            )
        ]

    def __str__(self):
        return f"{self.departamento} - {self.unidad}: {self.nro_item}"
