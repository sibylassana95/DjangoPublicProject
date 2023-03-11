from django.shortcuts import render


def Acceuil(request):
    return render(request, 'index.html')
