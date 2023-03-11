from django.contrib import admin
from .models import Produits


# Register your models here.
class AddminProduit(admin.ModelAdmin):
    list_display = ('id', 'nom', 'description', 'prix', 'stock')


admin.site.register(Produits, AddminProduit)
