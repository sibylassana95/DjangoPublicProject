from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'image')
    search_fields = ('titre',)


admin.site.register(Article, ArticleAdmin)
