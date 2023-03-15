from django.shortcuts import render
import random
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def passwords(request):

    minuscule = "abcdefghijklmnopqrstuvwxyz"
    majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nombre = "0987654321"
    symboles = "!@#$%&*?"

    generer = minuscule + majuscule + nombre + symboles

    longueurdumotdepasse = int(request.GET.get('number_characters'))

    password = "".join(random.sample(generer, longueurdumotdepasse))

    passwords_list = request.session.get('passwords_list', [])

    passwords_list.append(password)

    request.session['passwords_list'] = passwords_list
    passwords_list = request.session.get('passwords_list', [])

    return render(request, 'password.html', {"passwords": password, "passwords_list": passwords_list})


def passwords_list(request):

    passwords_list = request.session.get('passwords_list', [])

    return render(request, 'passwords_list.html', {"passwords_list": passwords_list})
