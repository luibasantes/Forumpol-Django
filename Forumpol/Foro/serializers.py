from rest_framework import serializers
from .models import Post,Plantas

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class PlantasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plantas
        fields = '__all__'