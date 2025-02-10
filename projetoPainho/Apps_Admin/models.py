import random
from django.contrib.auth.models import User
from django.db import models

class Doctor(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=20)
    especialidade = models.TextField(max_length=1000)
    crm = models.CharField(max_length=10)
    estado = models.CharField(max_length=2)
    def __str__(self):
        return f"Médico: {self.firstname} {self.lastname}"

class Hospital(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.TextField(max_length=500)
    telefone = models.CharField(max_length=20)
    especialidade = models.TextField(max_length=1000)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return f"Hospital: {self.nome} - {self.cidade}/{self.estado}"