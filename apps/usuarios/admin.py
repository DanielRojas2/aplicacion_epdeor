from django.contrib import admin
from .models.Departamento import Departamento
from .models.Unidad import Unidad
from .models.Puesto import Puesto
from .models.PerfilUsuario import PerfilUsuario

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['departamento']

@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    list_display = ['unidad']

@admin.register(Puesto)
class PuestoAdmin(admin.ModelAdmin):
    list_display = ['nro_item']

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'usuario']
