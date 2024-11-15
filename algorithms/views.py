from rest_framework import viewsets
from .serializer import AlgorithmSerializer
from .models import Algorithm

class AlgorithmViewSet(viewsets.ModelViewSet):
    queryset = Algorithm.objects.all()
    serializer_class = AlgorithmSerializer       
