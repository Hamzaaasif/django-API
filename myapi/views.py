from django.shortcuts import render
from rest_framework import generics
from .serializers import carsserializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import cars

class createcars(generics.ListCreateAPIView):
  queryset=cars.objects.all()
  serializer_class = carsserializers

  def perform_create(self,serializer):
    serializer.save()

class destroycars(generics.DestroyAPIView):
  #model=cars
  queryset=cars.objects.all()
  #serializer_class = carsserializers

  #queryset.delete()
  
  