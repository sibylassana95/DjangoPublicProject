from django.db import models
from django.urls import reverse


# Create your models here.
# base de donnees panel eleves

class Panel(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=150)
    ecole = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150, blank=True, null=True)
    profil = models.ImageField(upload_to='images', blank=True)

    class Meta:
        verbose_name = 'Panel',
        verbose_name_plural = 'Panels'

    def __str__(self):
        return self.nom


class Prof(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    matiere = models.CharField(max_length=150)
    salaire = models.IntegerField(blank=True, null=True)
    profil = models.ImageField(upload_to='images', blank=True)

    class Meta:
        verbose_name = 'Prof',
        verbose_name_plural = 'Profs'

    def __str__(self):
        return self.nom


def get_absolute_url(self):
    return reverse("user_detail", kwargs={"pk": self.pk})
