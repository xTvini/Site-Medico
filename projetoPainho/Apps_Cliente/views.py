from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Doctor, Hospital, Consulta

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
    medico_id = request.GET.get('medico_id', None)
    hospitais = Hospital.objects.filter(estado=selected_estado, especialidade=selected_especialidade)
    return render(request, "Clientes/marcarConsulta.html", {
        'estado': selected_estado,
        'especialidade': selected_especialidade,
        'hospitais': hospitais,
        'medico_id': medico_id
    })

@login_required
def calendario(request):
    consultas = Consulta.objects.filter(paciente=request.user)
    hospitais = Hospital.objects.all()
    medicos = Doctor.objects.all()
    dias_da_semana = ['DOM', 'SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB']
    hospital_id = request.GET.get('hospital_id', None)
    medico_id = request.GET.get('medico_id', None)

    return render(request, "Clientes/calendario.html", {
        "consultas": consultas,
        "hospitais": hospitais,
        "medicos": medicos,
        "dias_da_semana": dias_da_semana,
        "hospital_id": hospital_id,
        "medico_id": medico_id
    })

@login_required
def salvar_consulta(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        horario = request.POST.get('horario')
        hospital_id = request.POST.get('hospital_id')
        medico_id = request.POST.get('medico_id')

        if not hospital_id or not medico_id:
            messages.error(request, 'Hospital ou médico não selecionado.')
            return redirect('calendario')

        try:
            hospital = Hospital.objects.get(id=hospital_id)
            medico = Doctor.objects.get(id=medico_id)
            paciente = request.user

            consulta = Consulta(
                titulo=descricao,
                especialidade=medico.especialidade,
                data=data,
                horario=horario,
                hospital=hospital,
                medico=medico,
                paciente=paciente
            )
            consulta.save()

            messages.success(request, 'Consulta marcada com sucesso!')
            return redirect('calendario')
        except Hospital.DoesNotExist:
            messages.error(request, 'Hospital não encontrado.')
        except Doctor.DoesNotExist:
            messages.error(request, 'Médico não encontrado.')
        except Exception as e:
            messages.error(request, f'Erro ao marcar consulta: {str(e)}')

    return redirect('calendario')