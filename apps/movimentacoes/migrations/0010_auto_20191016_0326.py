# Generated by Django 2.2.4 on 2019-10-16 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimentacoes', '0009_remove_movimentacao_tombo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='quant',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Quantidade'),
        ),
    ]