from django.shortcuts import render
from rest_framework import viewsets
from .models import Plant, User
from .serializers import PlantSerializer, UserSerializer

class PlantView(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer