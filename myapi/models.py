from django.db import models
from django.urls import reverse

class cars(models.Model):
  objects=None
  brand= models.CharField(max_length=100)
  model=models.CharField(max_length=100)
  year=models.PositiveIntegerField()
  price=models.PositiveIntegerField()

  

  def __str__(self):
    return self.brand