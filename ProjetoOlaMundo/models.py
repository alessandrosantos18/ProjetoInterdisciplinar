from django.db import models
from django.template.defaultfilters import date
from django.utils.formats import date_format
from openshot_qt.classes.info import DATE



class Paciente(models.Model):
    
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    
    celular = models.CharField(
        max_length=11,
        null=False,
        blank=False
    )
    
    TelefoneFixo = models.CharField(
        max_length=8,
        null=False,
        blank=False
    )
    
    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
objetos = models.Manager

class exercicio_fisico (models.Model):
    
    nome_exercicio = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    data_exercicio = models.DateField(
        DATE,
        null=False,
        blank=False
    )
    
  
    
objetos = models.Manager

objetos = models.Manager

class Remedio (models.Model):
    
    nome_remedio = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    hora_evento = models.DateField(
        DATE,
        null=False,
        blank=False
    )
    
  
    
objetos = models.Manager

class Cuidador (models.Model):
    
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    data_nascimento = models.DateField(
        DATE,
        null=False,
        blank=False
    )
    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
     
objetos = models.Manager

class Agenda (models.Model):
    
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    data_evento = models.DateField(
        DATE,
        null=False,
        blank=False
    )
    
    descricao = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
  
    
objetos = models.Manager

