from datetime import datetime

from django.shortcuts import render


def home(request):
    context = {"date": datetime.today()}
    return render(request, "application/index.html", context)
