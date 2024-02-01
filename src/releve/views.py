from rest_framework import viewsets
from .models import Releve
from .serializers import ReleveSerializer

class ReleveViewSet(viewsets.ModelViewSet):
    queryset = Releve.objects.all()
    serializer_class = ReleveSerializer
