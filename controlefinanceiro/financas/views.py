from rest_framework import viewsets, generics, serializers
from financas.models import Receita, Despesa
from financas.serializers import ReceitaSerializer, DespesaSerializer
from django.db.models import Sum
from rest_framework.response import Response
from django.http import JsonResponse

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


class ResumoPorMes(generics.ListAPIView, serializers.ModelSerializer):
    """Endpoint para visualizar o resumo do mês"""

    def get(self, request, *args, **kwargs):
        
        receita_do_mes = Receita.objects.filter(data__year=self.kwargs['ano'], data__month=self.kwargs['mes']).aggregate(
             Sum('valor')) 
        despesa_do_mes = Despesa.objects.filter(data__year=self.kwargs['ano'], data__month=self.kwargs['mes']).aggregate(
            Sum('valor'))

        despesa_por_categoria = Despesa.objects.filter(data__year=self.kwargs['ano'], data__month=self.kwargs['mes']).values(
            'categoria').annotate(Sum('valor'))

        saldo = receita_do_mes['valor__sum'] - despesa_do_mes['valor__sum']

        def formataDespesasPorCategoria(self):
            despesas_formatadas = list(despesa_por_categoria)
            return despesas_formatadas

        
        return Response({
            "Receita mensal": f"R${receita_do_mes['valor__sum']}",
            "Despesa mensal": f"R${despesa_do_mes['valor__sum']}",
            "Despesas por categoria": f"{formataDespesasPorCategoria(self)}",
            "Saldo mensal": f"{saldo}",
           })