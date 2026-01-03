from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=120)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="produtos")
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    # FOTO
    foto = models.ImageField(upload_to="produtos/", blank=True, null=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome
