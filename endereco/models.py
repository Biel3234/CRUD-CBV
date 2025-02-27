from django.db import models

class Address(models.Model):
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=50) #rua
    bairro = models.CharField(max_length=30)
    localidade = models.CharField(max_length=30) #cidade
    uf = models.CharField(max_length=2) #estado
    
    
