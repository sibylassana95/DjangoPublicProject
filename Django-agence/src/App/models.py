from django.db import models


# Create your models here.
class Donnee(models.Model):
    nom = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='images', blank=True)

    class Meta:
        verbose_name = "Donnee",
        verbose_name_plural = "Donnees"

    def __str__(self):
        return self.nom


class Contact(models.Model):
    nom = models.CharField(max_length=150)
    email = models.EmailField(max_length=140)
    message = models.TextField()

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.nom