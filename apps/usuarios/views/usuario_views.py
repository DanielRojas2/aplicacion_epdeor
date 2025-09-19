from django.views.generic import ListView
from ..models.PerfilUsuario import PerfilUsuario
from ..decorators import group_required

@group_required("Encargado de sistemas")
class UsuariosListView(ListView):
    model = PerfilUsuario
    template_name = "usuarios/listar_usuarios.html"
