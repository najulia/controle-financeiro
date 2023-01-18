from rest_framework import serializers, fields
from financas.models import Receita, Despesa

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['id', 'descricao','valor','data']

class DespesaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Despesa
        fields = '__all__'

