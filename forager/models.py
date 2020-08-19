from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=40)
    wiki_url = models.URLField(max_length=2000)
    description = models.CharField(max_length=5000)
    first_similar_image = models.URLField(max_length=2000)
    second_similar_image = models.URLField(max_length=2000)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    plants = models.ManyToManyField(Plant, related_name='plants')

    def __str__(self):
        return self.username