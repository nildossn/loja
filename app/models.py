from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=30, primary_key=True)
    descricao = models.CharField(max_length=50)
    departamento = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
class Produto(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=50)
    preco_custo = models.FloatField()
    preco_venda = models.FloatField()
    fornecedor = models.CharField(max_length=20)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_DEFAULT, default=None)
