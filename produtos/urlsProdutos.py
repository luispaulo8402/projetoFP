from django.conf.urls import patterns, include, url

urlpatterns = patterns('produtos.views',
    url(r'^adicionar/$', 'produtoAdicionar'),
    url(r'^editar/(?P<pk>\d+)/$', 'produtoEditar'),
    url(r'^salvar/$', 'produtoSalvar'),
    url(r'^pesquisar/$', 'produtosPesquisar'),
    url(r'^excluir/(?P<pk>\d+)/$', 'produtoExcluir'),
    url(r'^$', 'produtoListar'),
)