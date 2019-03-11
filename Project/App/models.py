from django.db import models

# Create your models here.

class RecipeModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    date = models.DateField(default="")
    creator = models.CharField(max_length=40)

    def __str__(self):
     return f'{self.name}, {self.recipeMakeIdKey}'
