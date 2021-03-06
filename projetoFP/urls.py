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
    url(r'^i18n/', include('django.conf.urls.i18n')),
    #url(r'^pagseguro/', include('djpg.urls')),
)
