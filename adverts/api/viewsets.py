from rest_framework.viewsets import ModelViewSet
from .serializers import AnunciosSerializer
from adverts.models import Anuncios

class AnunciosViewSet(ModelViewSet):
    queryset = Anuncios.objects.all()
    serializer_class = AnunciosSerializer