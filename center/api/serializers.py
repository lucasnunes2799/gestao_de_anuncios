from rest_framework.serializers import ModelSerializer
from center.models import Empresa

class EmpresasSerializer(ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('id', 'nome', 'site', 'instagram', 'responsavel', 'telefone_responsavel')