# Generated by Django 3.2.9 on 2021-11-21 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0006_alter_empresa_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='telefone_responsavel',
            field=models.CharField(default=1, max_length=15, verbose_name='Nº telefone celular'),
            preserve_default=False,
        ),
    ]
