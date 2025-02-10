from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=20)
    def __str__(self):
        return f"Médico: {self.firstname} {self.lastname}"
# Create your models here.
