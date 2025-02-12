from django.urls import path
from . import views

urlpatterns = [
    path("Clientes/paginaInicialCliente/", views.PAGINAINICIALCLIENTE, name="paginaInicialCliente"),
    path("Clientes/marcarConsulta/", views.marcarConsulta , name='marcarConsulta'),
    path("Clientes/calendario/", views.calendario, name='calendario'),
    path("Clientes/salvar_consulta/", views.salvar_consulta, name='salvar_consulta')
]