from django.db import models

class Receita(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.FloatField(blank=False)
    data = models.DateField(null=False)


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


class Despesa(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.FloatField(blank=False)
    data = models.DateField(null=False)
    categoria = models.CharField(choices=CATEGORIAS, max_length=1, blank=True, default='O')


    @property
    def mes(self):
        return self.data.strftime('%m')
    
    @property
    def ano(self):
        return self.data.strftime('%Y')

