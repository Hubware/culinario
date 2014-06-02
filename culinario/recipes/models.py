from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = model.CharField(max_length = 255)
    photo = model.CharField(max_length = 255)