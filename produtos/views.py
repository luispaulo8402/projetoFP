# This Python file uses the following encoding: utf-8
# ANOTAÇÃO PARA USAR CARACTERES ESPECIAIS AQUI. (MESMO PARA ANOTAÇÕES.)

from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q #Queries complexas
from produtos.models import Produto

def produtoListar(request):
    produtos = Produto.objects.all()[0:10]

    # TESTE LOCAL PARA VERIFICAR SE A TABELA ESTA LISTANDO
    #produtos = []
    #produtos.append(Produto(nome='NOME1', email='MAIL', telefone='TELEFONE'))
    #produtos.append(Produto(nome='NOME2'))

    return render(request, 'produtos/listaProdutoss.html', {'produtos': produtos})


def produtoAdicionar(request):
    return render(request, 'produtos/formProdutos.html')

def produtoSalvar(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo', '0')

        try:
            produto = Produto.objects.get(pk=codigo)
        except:
            produto = Produto()

        produto.nome = request.POST.get('nome', '').upper()
        produto.quantidade = request.POST.get('quantidade', '').upper()
        produto.observacao = request.POST.get('observacao', '').upper()
        produto.modelo = request.POST.get('modelo', '').upper()

        produto.save()
        
    return HttpResponseRedirect('/produtos/')

def produtoPesquisar(request):
    if request.method == 'POST':
        textoBusca = request.POST.get('textoBusca', 'TUDO').upper()

        try:
            if textoBusca == 'TUDO':
                produtos = Produtos.objects.all()
            else: 
                produtos = Produto.objects.filter(
                    (Q(nome__contains=textoBusca) |  
                    Q(observacao__contains=textoBusca) | 
                    Q(modelo__contains=textoBusca))).order_by('-nome')  #BUSCA POR NOME OU OBSERVACAO OU MODELO... E É ORDENADO POR NOME.
        except:
            produtos = []

        return render(request, 'produtos/listaProdutos.html', {'produtos': produtos, 'textoBusca': textoBusca})

def produtoEditar(request, pk=0):
    try:
        produto = Produto.objects.get(pk=pk)
    except:
        return HttpResponseRedirect('/produtos/')

    return render(request, 'produtos/formProdutos.html', {'produto': produto})

def produtoExcluir(request, pk=0):
    try:
        produto = Produto.objects.get(pk=pk)
        produto.delete()
        return HttpResponseRedirect('/produtos/')
    except:
        return HttpResponseRedirect('/produtos/')
