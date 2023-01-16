from rest_framework import serializers

from .models import Curso, Avaliacao


#Só iremos apresentar aqui os campos que queremos mostrar.
class AvaliacaoSerializers(serializers.ModelSerializer):

    class Meta: #Criação de Configuração extra
        extra_kwargs = {
            'email': {'write_only': True} #Email será exigido somente quando for fazer cadastro / Vamos esconder quando for consultar.
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
        )


class CursoSerializers(serializers.ModelSerializer):

    class Meta: #Criação de Configuração extra
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
    )