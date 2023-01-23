from rest_framework import viewsets, generics
from rest_framework.views import APIView
from financas.models import Receita, Despesa
from financas.serializers import ReceitaSerializer, DespesaSerializer
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticatedOrReadOnly

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

class ResumoPorMes(APIView):
    """Endpoint para visualizar despesas conforme o mês"""

    def get(self,request,mes,ano):
        receita_mes =  Receita.objects.filter(data__month = mes,data__year =ano).aggregate(TOTAL = Sum('valor'))['TOTAL']
        despesa_mes =  Despesa.objects.filter(data__month = mes,data__year =ano).aggregate(TOTAL = Sum('valor'))['TOTAL']
        total =  receita_mes - despesa_mes
        categoria = Despesa.objects.filter(data__month = mes, data__year = ano,).values('categoria').annotate(total = Sum('valor'))
        return Response ({
            'Receita do Mês' : f"R$ {receita_mes}",
            'Despesa do Mês' : f"R$ {despesa_mes}",
            'Saldo restante' : f"R$ {total}",
            'Gasto por categoria' : categoria,
        
        })

class IsOwnerOrReadOnly(BasePermission):
    """Impede que sejam realizadas operações de PUT, POST e DELETE"""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True