from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
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
            'username',
            'plants'
        )

class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        # if password is not None:
        #     instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')