from django.contrib import admin
from .models import Donnee, Contact


# Register your models here.
class AddminDonnee(admin.ModelAdmin):
    list_display = ('id', 'nom', 'description')


admin.site.register(Donnee, AddminDonnee)


class Addcontact(admin.ModelAdmin):
    list_display = ('id', 'nom', 'email', 'message')


admin.site.register(Contact, Addcontact)
