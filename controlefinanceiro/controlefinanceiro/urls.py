"""controlefinanceiro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from financas.views import ReceitaViewSet, DespesaViewSet, ListaDespesasPorMes, ResumoPorMes
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('receitas', ReceitaViewSet, basename='receitas')
router.register('despesas', DespesaViewSet, basename='despesas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('despesas/<str:ano>/<str:mes>/', ListaDespesasPorMes.as_view()),
    path('resumo/<str:ano>/<str:mes>/', ResumoPorMes.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
