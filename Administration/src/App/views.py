from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.

from django.db.models import Count
from django.views.generic import DetailView

from App.models import Panel, Prof


def panel(request):
    product = Panel.objects.all()
    total = Panel.objects.aggregate(Count('nom'))
    print(total)
    total = total.get("nom__count")
    print(total)
    total1 = Prof.objects.aggregate(Count('nom'))
    print(total1)
    total1 = total1.get("nom__count")
    print(total1)
    context = {
        "produits": product,
        "total": total,
        "total1": total1,

    }

    return render(request, "app/panel.html", context)


def eleve(request):
    product = Panel.objects.all()
    context = {
        "produits": product,

    }
    return render(request, "app/eleves.html", context)


def prof(request):
    product = Prof.objects.all()

    context = {
        "produits": product,

    }
    return render(request, "app/prof.html", context)



