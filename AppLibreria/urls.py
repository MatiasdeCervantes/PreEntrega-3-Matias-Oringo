from django.urls import path
from AppLibreria.views import *

urlpatterns = [
    path("autor/", crear_autor),
    path("clientes/", crear_cliente),
    path("subgeneros/", crear_subgenero),
    path("ver_clientes", ver_clientes, name="Clientes"),
    path("ver_autores", ver_autores, name="Autores"),
    path("ver_subgeneros", ver_subgeneros, name="Subgeneros"),
    path("buscar_cliente/", buscar_cliente, name="Buscar_cliente"),
    path("buscar_subgenero/", buscar_subgenero, name="Buscar_subgenero"),
    path("buscar_autor/", buscar_autor, name="Buscar_autor"),
    path("", inicio, name="Home"),
]