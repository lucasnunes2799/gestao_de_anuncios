# Generated by Django 3.2.9 on 2021-11-19 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('site', models.TextField()),
                ('instagram', models.TextField()),
                ('responsavel', models.CharField(max_length=40)),
                ('telefone_responsavel', models.TextField()),
            ],
        ),
    ]
