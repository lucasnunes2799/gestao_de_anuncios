# Generated by Django 3.2.9 on 2021-11-21 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0007_rename_nome_anuncios_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncios',
            name='nome',
            field=models.CharField(default=1, max_length=150, verbose_name='Nome do Anuncio'),
            preserve_default=False,
        ),
    ]
