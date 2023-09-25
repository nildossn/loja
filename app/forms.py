from django.forms import ModelForm
from app.models import Produto, Categoria
from django import forms

# Create the form class.
class escolha_categoria(forms.Form):
    categorias = Categoria.objects.all()
    opcoes_categoria = [(cat.nome, cat.nome) for cat in categorias]

    categoria = forms.ChoiceField(choices=opcoes_categoria, widget=forms.Select(attrs={'class': 'form-control'}))

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "descricao", "preco_custo", "preco_venda", "fornecedor", "categoria"]

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome", "descricao", "departamento"]