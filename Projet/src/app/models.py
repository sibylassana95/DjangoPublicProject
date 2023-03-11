from django.db import models
from django.urls import reverse


# base de donnees Produits
class Produits(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=150)
    description = models.TextField()
    prix = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True)

    class Meta:
        verbose_name = 'Produit',
        verbose_name_plural = 'Produits'

    def __str__(self):
        return self.nom

    # Recuperation de l'ID

    def get_absolute_url(self):
        return reverse("update", kwargs={"my_id": self.pk})
