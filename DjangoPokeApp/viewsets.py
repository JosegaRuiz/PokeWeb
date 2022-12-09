from rest_framework import viewsets
from .models import Type
from .serializer import TypeSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
