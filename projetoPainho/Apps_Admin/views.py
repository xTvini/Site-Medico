from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from . models import Doctor,Hospital

def index(request):
    return redirect("PIAdmin")

@login_required
def Doctor_create(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        sobrenome = request.POST["sobrenome"]
        email = request.POST["email"]
        telefone = request.POST["telefone"]
        especialidade = request.POST["especialidade"]
        crm = request.POST["crm"]
        estado = request.POST["estado"]
        doctor = Doctor(
            firstname=nome,
            lastname=sobrenome,
            email=email,
            telephone=telefone,
            especialidade=especialidade,
            crm=crm,
            estado=estado,
        )
        doctor.save()
        messages.info(request, "Medico criado com sucesso")
        return redirect("PIAdmin")
    else:
        return render(request, "Admin/cadastrarMedico.html")

@login_required
def Doctor_delete(request,id):
    doctor = get_object_or_404(Doctor,id=id)
    if request.methd == "POST":
        doctor.delete()
        return redirect("")
    return render(request, "Admin/deletarMedico",{"doctor":doctor})
    
@login_required
def Doctor_edit(request, id):
    doctor = get_object_or_404(Doctor,id=id)
    if request.method == "POST":
        doctor.firstname = request.POST
        doctor.firstname = request.POST["nome"]
        doctor.lastname = request.POST["sobrenome"]
        doctor.email = request.POST["email"]
        doctor.telephone = request.POST["telefone"]
        doctor.especialidade=request.POST["especialidade"]
        doctor.crm=request.POST["crm"],
        doctor.estado=request.POST["estado"],
        doctor.save()
        messages.info(request, "Cliente editado com sucesso")
        return redirect("PIAdmin")
    else:
        return render(request, "Admin/editarMedico.html", {"doctor": doctor})
    

