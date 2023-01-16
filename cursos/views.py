from rest_framework import generics

from .models import Curso, Avaliacao
from .serializers import CursoSerializers, AvaliacaoSerializers


#Get e Post
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers

#Get, Put e Delete pois dependem de um 'ID'
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers

#Get e Post
class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers

#Get, Put e Delete pois dependem de um 'ID'
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers