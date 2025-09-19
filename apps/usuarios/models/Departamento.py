from django.db import models

class Departamento(models.Model):
    departamento = models.CharField(
        max_length=65,
        blank=False,
        null=False,
        unique=True
    )

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return self.departamento
