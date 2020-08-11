from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Plant, User

class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = (
            'id',
            'url',
            'name', 
            'wiki_url', 
            'description',
            'first_similar_image', 
            'second_similar_image'
        )

class UserSerializer(WritableNestedModelSerializer):
    plants = PlantSerializer(many=True)
    class Meta: 
        model = User
        fields = (
            'id',
            'url',
            'name',
            'plants'
        )