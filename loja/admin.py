from django.contrib import admin
from .models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "preco", "ativo", "criado_em")
    list_filter = ("ativo", "categoria")
    search_fields = ("nome", "descricao")
