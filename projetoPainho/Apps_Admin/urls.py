from django.urls import path

from . import views

urlpatterns = [
    path("Admin/cadastrarMedico/", views.Doctor_create, name="cadastrarMedico"),
    path("Admin/deletarMedico/", views.Doctor_delete, name="deletarMedico"),
    path("Admin/editarMedico/", views.Doctor_edit, name="editarMedico"),
    path("Admin/PIAdmin/", views.index, name="PIAdmin"),

]