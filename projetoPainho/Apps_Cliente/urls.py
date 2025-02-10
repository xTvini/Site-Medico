from django.urls import path

from . import views

urlpatterns = [
    path("Cliente/PICliente", views.index, name="PICliente"),
]