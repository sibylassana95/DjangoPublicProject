from django.urls import path

from App.views import panel, eleve, prof

urlpatterns = [
    path('panel/', panel, name="panel"),
    path('eleve/', eleve, name="eleve"),
    path('prof/', prof, name="prof"),


]
