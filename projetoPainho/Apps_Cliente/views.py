from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Apps_Admin.models import Doctor, Hospital

@login_required
def PAGINAINICIALCLIENTE(request):
    estado = Doctor.objects.values_list('estado', flat=True).distinct()
    especialidades = Doctor.objects.values_list('especialidade', flat=True).distinct()
    doctors = None
    selected_especialidade = request.GET.get('especialidade', None)
    selected_estado = request.GET.get('estado', None)

    if selected_especialidade and selected_estado:
        doctors = Doctor.objects.filter(especialidade=selected_especialidade, estado=selected_estado)

    return render(request, "Clientes/paginaInicialCliente.html", {
        'especialidades': especialidades,
        'doctors': doctors,
        'estado': estado
    })

@login_required
def marcarConsulta(request):
    selected_estado = request.GET.get('estado', None)
    selected_especialidade = request.GET.get('especialidade', None)

    # Filtra os hospitais que possuem a especialidade e estão no estado correto
    hospitais = Hospital.objects.filter(estado=selected_estado, especialidade=selected_especialidade)

    return render(request, "Clientes/marcarConsulta.html", {'estado': selected_estado,'especialidade': selected_especialidade,'hospitais': hospitais})
