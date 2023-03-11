from django.urls import path

from app.views import quiz

urlpatterns = [
    path('', quiz, name="quiz")
]
