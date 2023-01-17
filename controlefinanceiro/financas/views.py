from rest_framework import viewsets, request
from financas.models import Receita, Despesa
from financas.serializers import ReceitaSerializer, DespesaSerializer

class ReceitaViewSet(viewsets.ModelViewSet):
    """Endpoint para visualizar ou editar receitas"""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    filterset_fields = ['descricao']
    search_fields = ['descircao']

class DespesaViewSet(viewsets.ModelViewSet):
    """Endpoint para visualizar ou editar despesas"""
    queryset = Despesa.objects.all().order_by('data')
    serializer_class = DespesaSerializer
    filterset_fields = ['descricao']
    search_fields = ['descircao']