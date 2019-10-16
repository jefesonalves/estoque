from django.db import models

class Requisitante(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    setor = models.CharField(max_length=200, verbose_name='Setor')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    email = models.CharField(max_length=50, verbose_name='e-mail')

    class Meta:
        verbose_name_plural = '01 - Cadastro de Requisitantes'

    def __str__(self):
        return self.nome