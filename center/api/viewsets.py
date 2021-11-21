from rest_framework.viewsets import ModelViewSet
from .serializers import EmpresasSerializer
from center.models import Empresa

class EmpresasViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresasSerializer