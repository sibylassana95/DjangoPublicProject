from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
    path('ajouter/', views.ajouter_article, name='ajouter_article'),
    path('modifier/<int:id_article>/', views.modifier_article, name='modifier_article'),
    path('supprimer/<int:id_article>/', views.supprimer_article, name='supprimer_article'),
    path('<int:id_article>/', views.detail_article, name='detail_article'),
]
