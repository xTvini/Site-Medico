from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Doctor, Hospital, Consulta
import json

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

@login_required
def calendario(request):
    consultas = Consulta.objects.all()

    eventos = [
        {
            "titulo": consulta.titulo,
            "descricao": f"Médico: {consulta.medico.firstname} ({consulta.medico.crm} - {consulta.medico.estado})",
            "data": consulta.data.strftime("%Y-%m-%d"),
            "horario": consulta.horario.strftime("%H:%M") if consulta.horario else "",
            "hospital": consulta.hospital.nome,
        }
        for consulta in consultas
    ]
    dias_da_semana = ['DOM', 'SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB']
    return render(request, "Clientes/calendario.html", {"eventos_json": json.dumps(eventos), "dias_da_semana": dias_da_semana})