from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views.usuario_views import UsuariosListView


urlpatterns = [
    path('iniciar-sesion/', auth_views.LoginView.as_view(), name='iniciar_sesion'),
    path('cerrar-sesion/', auth_views.LogoutView.as_view(), name='cerrar_sesion'),

    path('', UsuariosListView.as_view(), name='usuarios'),
]
