from django.db import models
import datetime

CATEGORIAS = [ 
        ('A','alimentacao'),
        ('S', 'saude'),
        ('M', 'moradia'),
        ('T','transporte'),
        ('E','educacao'),
        ('L','lazer'),
        ('I','imprevistos'),
        ('O','outras'),
        ]

class Receita(models.Model):
    descricao = models.CharField(max_length=100, unique=True, error_messages={'unique': "Você já cadastrou essa receita antes"})
    valor = models.FloatField(blank=False)
    data = models.DateField(default=datetime.date.today, blank=False)

class Despesa(models.Model):
    descricao = models.CharField(max_length=100, unique=True, error_messages={'unique': "Você já cadastrou essa despesa antes"})
    valor = models.FloatField(blank=False)
    data = models.DateField(default=datetime.date.today, blank=False)
    categoria = models.CharField(choices=CATEGORIAS, max_length=1, blank=True, default='O')
