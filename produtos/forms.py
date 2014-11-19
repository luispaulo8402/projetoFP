from django import forms
from produtos.models import Produto

class produtoForm(forms.Form):
    nome = forms.CharField(max_length=100, required=True)
    quantidade = forms.CharField(max_length=10, required=True)
    observacao = forms.CharField(max_length=300, required=True)
    modelo = forms.CharField(max_length=50, required=True)