from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from ..models import Post, Thread, User, Recurso, Archivo

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['owner','aprobado']

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'
        read_only_fields = ['respuestas']

class RecursoSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Recurso
        fields = '__all__'

class ArchivoSerializer(mongoserializers.EmbeddedDocumentSerializer):
    class Meta:
        model = Archivo
        fields = '__all__'