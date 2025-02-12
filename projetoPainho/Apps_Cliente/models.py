from django.db import models
from django.contrib.auth.models import User
from Apps_Admin.models import Doctor, Hospital

class Consulta(models.Model):
    titulo = models.CharField(max_length=200)
    especialidade = models.CharField(max_length=100, blank=True)
    data = models.DateField()
    horario = models.TimeField(blank=True, null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    medico = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.titulo} - {self.medico.nome} - {self.data} {self.horario}"
