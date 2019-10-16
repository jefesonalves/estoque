from django.db import models

class Marca(models.Model):
    descricao_marca = models.CharField(max_length=100, verbose_name='Marca', help_text='Descrição da marca')

    class Meta:
        verbose_name_plural = '01 - Cadastro de marcas'

    def __str__(self):
        return self.descricao_marca
        return "{0}".format(self.descricao_marca)

class UnidadeMedida(models.Model):
    unidade = models.CharField(max_length=50, verbose_name='Descrição', help_text='Descrição da unidade de medida')

    class Meta:
        verbose_name_plural = '02 - Cadastro de unidades de medida'

    def __str__(self):        
        return "{0}".format(self.unidade)

class Produto(models.Model):
    descricao_produto = models.CharField(max_length=150, verbose_name='Descrição', help_text='Descrição do produto')
    descricao_marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name='Marca', help_text='Marca')
    unidade = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE, verbose_name='Unidade', help_text='Unidade')
    num_serie = models.CharField(max_length=150, verbose_name='Número de série', help_text='Número de série')

    class Meta:
        verbose_name_plural = '03 - Cadastro de produtos'

    def __str__(self):
        return "{0}".format(self.descricao_produto)