from django.db import models
from django.utils.translation import ugettext_lazy as _

class Produto (models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=500)
    observacao = models.CharField(max_length=200)
    modelo = models.CharField(max_length=100)
    class Meta:
        verbose_name = _('produto')
        verbose_name_plural = _('produtos')

    def __unicode__(self): 
        return self.nome 