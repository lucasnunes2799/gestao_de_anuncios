from rest_framework.serializers import ModelSerializer
from adverts.models import Anuncios

class AnunciosSerializer(ModelSerializer):
    class Meta:
        model = Anuncios
        fields = ('id','nome', 'data_inicial', 'data_final', 'valor', 'arquivo', 'tempo', 'Empresa')