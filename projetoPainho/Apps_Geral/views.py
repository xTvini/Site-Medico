from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login
from rolepermissions.checkers import has_role
from projetoPainho.roles import Cliente, Admin
from .models import Cliente as ClienteModel, Admin as AdminModel
from django.contrib import messages
from rolepermissions.roles import assign_role
from django.utils.translation import gettext as _


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'Geral/cadastro.html')
    else:
        user_name = request.POST.get('username')
        user_email = request.POST.get('email')
        senha = request.POST.get('senha')
        user_type = request.POST.get('user_type')
        if User.objects.filter(username=user_name).exists():
            messages.error(request, _("Já existe um usuário com esse nome"))
            return redirect("cadastro")  
        user = User.objects.create_user(username=user_name, email=user_email, password=senha)
        if user_type == 'Admin':
            assign_role(user, Admin)
            AdminModel.objects.create(usuario=user,  email=user_email)
        elif user_type == 'Cliente':
            assign_role(user, Cliente)
            ClienteModel.objects.create(usuario=user,  email=user_email)
        else:
            messages.error(request, _("Papel do usuário não especificado. Selecione 'Administrador' ou 'Cliente'."))
            return redirect("cadastro")
        messages.success(request, _("Usuário cadastrado com sucesso. Agora faça login."))
        return redirect("login") 
def login(request):
    if request.method == 'GET':
        return render(request, 'Geral/login.html')
    else:
        user_name = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=user_name, password=senha)
        if user:
            django_login(request, user)
            if has_role(user, Admin):
                return redirect("paginaInicialAdmin")
            elif has_role(user, Cliente):
                return redirect("paginaInicialCliente")
            else:
                messages.error(request, _("O usuário não tem um papel definido."))
                return redirect("login")
        else:
            messages.error(request, _("Usuário ou senha incorretos. Por favor, tente novamente."))
            return redirect("login")
def plataforma(request):
    if request.user.is_authenticated:  
        if has_role(request.user, Admin):
            return redirect("paginaInicialAdmin")
        elif has_role(request.user, Cliente):
            return redirect("paginaInicialCliente")
    return HttpResponse(_('Você precisa estar logado'))
