from django.contrib import admin
from financas.models import Receita

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao')

admin.site.register(Receita, ReceitaAdmin)
