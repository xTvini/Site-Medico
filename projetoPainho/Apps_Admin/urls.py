from django.urls import path

from . import views

urlpatterns = [
    path("Admin/paginaInicialAdmin/", views.PIAdmin, name="paginaInicialAdmin"),
    path("Admin/cadastrarMedico/", views.Doctor_create, name="cadastrarMedico"),
    path("Admin/deletarMedico/<int:id>/", views.Doctor_delete, name="deletarMedico"),
    path("Admin/editarMedico/<int:id>/", views.Doctor_edit, name="editarMedico"),
    path("Admin/cadastrarHospital/", views.Hospital_Create, name="cadastrarHospital"),
    path("Admin/deletarHospitais/<int:id>/", views.Hospital_delete, name="deletarHospital"),
    path("Admin/editarHospital/<int:id>/", views.Hospital_edit, name="editarHospital"),
]
