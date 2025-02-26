from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from . models import Doctor,Hospital

@login_required
def PIAdmin(request):
    doctor = Doctor.objects.all()
    hospital = Hospital.objects.all()
    return render(request,"Admin\paginaInicialAdmin.html",{"doctor": doctor,"hospital": hospital})

@login_required
def Doctor_create(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        sobrenome = request.POST["sobrenome"]
        telefone = request.POST["telefone"]
        especialidade = request.POST["especialidade"]
        crm = request.POST["crm"]
        estado = request.POST["estado"]
        doctor = Doctor(
            firstname=nome,
            lastname=sobrenome,
            telephone=telefone,
            especialidade=especialidade,
            crm=crm,
            estado=estado,
        )
        doctor.save()
        messages.info(request, "Medico criado com sucesso")
        return redirect("paginaInicialAdmin")
    else:
        return render(request, "Admin/cadastrarMedico.html")

@login_required
def Hospital_Create(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        endereco = request.POST["endereco"]
        telefone = request.POST["telefone"]
        especialidade = request.POST["especialidade"]
        cidade = request.POST["cidade"]
        estado = request.POST["estado"]
        hospital = Hospital(
            nome = nome,
            endereco = endereco,
            telefone = telefone,
            especialidade = especialidade,
            cidade = cidade,
            estado = estado,
        )
        hospital.save()
        messages.info(request, "Medico criado com sucesso")
        return redirect("paginaInicialAdmin")
    else:
        return render(request, "Admin/cadastrarHospital.html")
        
@login_required
def Doctor_delete(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == "POST":
        doctor.delete()
        return redirect("paginaInicialAdmin")
    return render(request, "Admin/deletarMedico.html", {"doctor": doctor})

@login_required
def Doctor_edit(request, id):
    doctor = get_object_or_404(Doctor, id=id)  # Busca o médico pelo ID
    if request.method == "POST":
        doctor.firstname = request.POST["nome"]
        doctor.lastname = request.POST["sobrenome"]
        doctor.telephone = request.POST["telefone"]
        doctor.especialidade = request.POST["especialidade"]
        doctor.crm = request.POST["crm"]
        doctor.estado = request.POST["estado"]
        doctor.save()
        messages.info(request, "Médico editado com sucesso")
        return redirect("paginaInicialAdmin")
    else:
        return render(request, "Admin/editarMedico.html", {"doctor": doctor})