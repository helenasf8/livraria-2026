from rest_framework.serializers import ModelSerializer

from core.models import Livro


class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ('id', 'titulo', 'preco')


class LivroRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

# list = apenas id retrieve = lista todos
