from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Editora, Livro
from core.serializers import CategoriaSerializer, EditoraSerializer, LivroSerializer
from rest_framework.permissions import IsAuthenticated

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
