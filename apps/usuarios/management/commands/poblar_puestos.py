import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from ...models.Puesto import Puesto, Departamento, Unidad

class Command(BaseCommand):
    help = "Poblar la tabla Puesto desde un archivo JSON"

    def add_arguments(self, parser):
        parser.add_argument(
            "archivo", nargs="?", type=str,
            help="Ruta al archivo JSON con puestos (opcional)"
        )

    def handle(self, *args, **options):
        archivo = options["archivo"]

        if not archivo:
            archivo = os.path.join(settings.BASE_DIR, "usuarios", "fixtures", "puestos.json")

        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error al abrir JSON {archivo}: {e}"))
            return

        objetos = []
        errores = 0

        for item in data:
            try:
                nro_item = item["nro_item"]
                dep_nombre = item["departamento"]
                uni_nombre = item["unidad"]

                departamento = Departamento.objects.filter(departamento=dep_nombre).first()
                unidad = Unidad.objects.filter(unidad=uni_nombre).first()

                if not departamento or not unidad:
                    errores += 1
                    self.stderr.write(self.style.WARNING(
                        f"Saltado: {nro_item} porque no existe departamento='{dep_nombre}' o unidad='{uni_nombre}'"
                    ))
                    continue

                objetos.append(Puesto(nro_item=nro_item, departamento=departamento, unidad=unidad))

            except KeyError as e:
                errores += 1
                self.stderr.write(self.style.WARNING(f"Falta campo {e} en {item}"))

        Puesto.objects.bulk_create(objetos, ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS(
            f"Se cargaron {len(objetos)} puestos (saltados {errores})."
        ))
