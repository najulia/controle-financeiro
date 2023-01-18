from rest_framework import viewsets, generics
from financas.models import Receita, Despesa
from financas.serializers import ReceitaSerializer, DespesaSerializer

class ReceitaViewSet(viewsets.ModelViewSet):
    """Endpoint para visualizar ou editar receitas"""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    filterset_fields = ['descricao', 'data']
    search_fields = ['descricao']

class DespesaViewSet(viewsets.ModelViewSet):
    """Endpoint para visualizar ou editar despesas"""
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    filterset_fields = ['descricao']
    search_fields = ['descricao']

class ListaDespesasPorMes(generics.ListAPIView):
    serializer_class = DespesaSerializer

    def get_queryset(self):
        """Endpoint para visualizar despesas conforme o mês"""
        return Despesa.objects.filter(data__year=self.kwargs['ano'], data__month=self.kwargs['mes'])
