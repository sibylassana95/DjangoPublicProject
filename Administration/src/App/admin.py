from django.contrib import admin
from .models import Panel, Prof


class AddminPanel(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'ecole')


class AddminPanel2(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'matiere', 'salaire')


admin.site.register(Prof, AddminPanel2)
admin.site.register(Panel, AddminPanel)