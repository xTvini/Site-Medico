from django.urls import path

from . import views

urlpatterns = [
    path("Clientes/paginaInicialCliente/", views.PAGINAINICIALCLIENTE, name="paginaInicialCliente"),
    path("Clientes/marcarConsulta", views.marcarConsulta , name='marcarConsulta')
]