# Generated by Django 2.2.4 on 2019-10-15 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0001_initial'),
        ('requisitantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(help_text='Tipo de Entrada', max_length=100, verbose_name='Tipo de Entrada')),
            ],
            options={
                'verbose_name_plural': '01 - Cadastro de tipos de entrada',
            },
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setor', models.CharField(blank=True, max_length=150, verbose_name='Nome do setor')),
                ('quant', models.DecimalField(decimal_places=3, max_digits=9, verbose_name='Quantidade')),
                ('tombo', models.CharField(blank=True, max_length=150, verbose_name='Número do tombo')),
                ('num_serie_produto', models.CharField(blank=True, max_length=150, verbose_name='Número de série')),
                ('descricao_marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Marca', verbose_name='Descrição da Marca')),
                ('descricao_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Produto', verbose_name='Descrição do Produto')),
                ('nome', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='requisitantes.Requisitante', verbose_name='Nome do Usuário')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movimentacoes.Tipo', verbose_name='Tipo de Entrada')),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unidade_medida', to='produtos.Produto', verbose_name='Tipo de Unidade')),
            ],
            options={
                'verbose_name_plural': '02 - Movimentações',
            },
        ),
    ]
