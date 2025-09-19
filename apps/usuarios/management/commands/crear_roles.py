from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = "Crea los grupos base del sistema"

    def handle(self, *args, **options):
        roles = [
            "Solicitante",
            "Encargado de sistemas",
            "Encargado de almacenes",
            "Encargado de archivos",
        ]
        for r in roles:
            g, created = Group.objects.get_or_create(name=r)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Grupo creado: {r}"))
            else:
                self.stdout.write(f"Grupo ya existía: {r}")
