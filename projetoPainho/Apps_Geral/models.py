from django.db import models
from django.contrib.auth.models import User
import random

User.add_to_class('role', models.CharField(max_length=50, default='Cliente', choices=[('Cliente', 'Cliente'), ('Admin', 'Admin')]))
def generate_unique_ra():
    while True:
        ra = str(random.randint(10**9, 10**10 - 1))  # Gera um RA de 10 dígitos
        if not Cliente.objects.filter(ra=ra).exists() and not Admin.objects.filter(ra=ra).exists():
            return ra

class Admin(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Admin', null=True)
    email= models.EmailField(null=True, max_length=254)
    ra = models.CharField(max_length=10, unique=True, default=generate_unique_ra)  # Função explícita para RA

    def __str__(self):
        return self.usuario.username
    
class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Cliente", null=True)
    email = models.EmailField(null=True, max_length=254)  # Garantir emails únicos
    ra = models.CharField(max_length=10, unique=True, default=generate_unique_ra)       
     # Função explícita para RA

    def __str__(self):
        return f"{self.usuario.username}"