from django.db import models
from center.models import Empresa

class Anuncios(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome do Anuncio')
    data_inicial = models.DateField()
    data_final = models.DateField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    arquivo = models.FileField(upload_to='adverts', null=True, blank=True, verbose_name='Upload de Imagem ou Video')
    tempo = models.TextField(verbose_name='Tempo de exibição em segundos')
    Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)


    def  str  (self):
            return self.nome