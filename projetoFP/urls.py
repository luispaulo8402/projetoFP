""" 
@edsonlb
https://www.facebook.com/groups/pythonmania/
"""

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.index'),
    url(r'^pessoas/', include('pessoas.urlsPessoas')),
    url(r'^caixas/', include('caixas.urlsCaixas')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^produtos/', include('produtos.urlsProdutos')),
    #url(r'^pagseguro/', include('djpg.urls')),
                       url(r'^il8n/', include('django.conf.urls.il8n')),
)
