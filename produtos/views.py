# This Python file uses the following encoding: utf-8
# ANOTAÇÃO PARA USAR CARACTERES ESPECIAIS AQUI. (MESMO PARA ANOTAÇÕES.)

from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from django.db.models import Q #Queries complexas
from produtos.models import Produto
from produtos.forms import produtoForm
import string



def produtoAdicionar(request):
    form = produtoForm()
    return render(request,'formProdutos.html',{'form':form})

def produtoSalvar(request):
     if request.method == 'POST':
        form = produtoForm(request.POST)

        if form.is_valid():
            
            if(form.data['pk']):
                produto = Produto.objects.get(pk=form.data['pk'])
                produto.nome=string.replace(string.replace(form.data['nome'],"(u'",""),"',)","")
                produto.quantidade=string.replace(string.replace(form.data['quantidade'],"(u'",""),"',)","")
                produto.observacao=string.replace(string.replace(form.data['observacao'],"(u'",""),"',)","")
                produto.modelo=string.replace(string.replace(form.data['modelo'],"(u'",""),"',)","")
                
            else:
                
                produto = Produto(
                    nome=form.data['nome'], 
                    quantidade=form.data['quantidade'],
                    observacao=form.data['observacao'],
                    modelo=form.data['modelo']
                )
                
            produto.save()
            return HttpResponseRedirect('/produtos/')
        else:
            return render(request,'formProdutos.html',{'form':form})

def produtoPesquisar(request):
    if request.method == 'POST':
        textoBusca = request.POST.get('textoBusca', 'TUDO').upper()

        try:
            if textoBusca == 'TUDO':
                produtos = Produto.objects.all()
            else: 
                produtos = Produto.objects.filter(
                    (Q(nome__contains=textoBusca) |  
                    Q(observacao__contains=textoBusca) | 
                    Q(modelo__contains=textoBusca))).order_by('-nome')  #BUSCA POR NOME OU OBSERVACAO OU MODELO... E É ORDENADO POR NOME.
        except:
            produtos = []

        return render(request, 'listaProdutos.html', {'produtos': produtos, 'textoBusca': textoBusca})

def produtoEditar(request, pk=0):

        produto = Produto.objects.get(pk=pk)
        
        data = {
            'nome':produto.nome,
            'quantidade':produto.quantidade,
            'observacao':produto.observacao,
            'modelo':produto.modelo
               }
        
        form = produtoForm(data)
        return render(request,'formProdutos.html',{'form':form,'pk':pk})


def produtoExcluir(request, pk=0):
    try:
        produto = Produto.objects.get(pk=pk)
        produto.delete()
        return HttpResponseRedirect('/produtos/')
    except:
        return HttpResponseRedirect('/produtos/')
