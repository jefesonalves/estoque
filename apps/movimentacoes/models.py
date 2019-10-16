from django.db import models
from apps.produtos.models import Marca, UnidadeMedida, Produto
from apps.requisitantes.models import Requisitante

class Tipo(models.Model):
    descricao = models.CharField(max_length=100, verbose_name='Tipo de Entrada', help_text='Tipo de Entrada')

    class Meta:
        verbose_name_plural = '01 - Cadastro de tipos de entrada'

    def __str__(self):
        return self.descricao

class Movimentacao(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, verbose_name='Tipo de Movimentação')
    setor = models.CharField(max_length=150, blank=True, verbose_name='Setor do Destinatário')
    nome = models.ForeignKey(Requisitante, blank=True, on_delete=models.CASCADE, verbose_name='Nome do Requisitante')
    quant = models.DecimalField(max_digits=9, decimal_places=3, verbose_name='Quantidade')
    descricao_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Descrição do Produto')
    descricao_marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name='Descrição da Marca')
    unidade = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE, verbose_name='Unidade de Medida')
    num_serie_produto = models.CharField(max_length=150, blank=True, verbose_name='Número de Série')


    class Meta:
        verbose_name_plural = '02 - Movimentações'

    def __str__(self):
        return self.setor
    # concatenar Tipo de entrada, quantidade e descrição