# Generated by Django 3.2.9 on 2021-11-21 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0005_auto_20211120_2112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncios',
            old_name='Empresa',
            new_name='nome',
        ),
    ]
