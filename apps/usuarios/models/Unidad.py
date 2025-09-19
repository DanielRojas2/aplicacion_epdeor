from django.db import models

class Unidad(models.Model):
    unidad = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        unique=True
    )

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"

    def __str__(self):
        return self.unidad
