# Generated by Django 3.2.9 on 2021-11-19 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0002_alter_empresa_telefone_responsavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='instagram',
            field=models.TextField(verbose_name='Instagram da empresa'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nome',
            field=models.CharField(max_length=150, verbose_name='Razao Social da empresa'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='responsavel',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='site',
            field=models.TextField(verbose_name='Site da empresa'),
        ),
    ]
