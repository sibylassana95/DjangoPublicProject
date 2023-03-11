from django.db import models


class Article(models.Model):
    titre = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    contenu = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.titre
