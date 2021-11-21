from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Razao Social da empresa')
    site = models.TextField(verbose_name='Site da empresa')
    instagram = models.TextField(verbose_name='Instagram da empresa')
    responsavel = models.CharField(max_length=60)
    telefone_responsavel = models.CharField(max_length=15, verbose_name='Nº telefone celular')

    def  str  (self):
            return self.nome
