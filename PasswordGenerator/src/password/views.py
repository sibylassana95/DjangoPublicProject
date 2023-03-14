from django.shortcuts import render
import random
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def passwords(request):
    minuscule = "abcdefghijklmnopqrstuvwxyz"
    majuscule= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nombre = "0987654321"
    symboles= "!@#$%&*?"

    generer = minuscule + majuscule + nombre + symboles

    longueurdumotdepasse = int(request.GET.get('number_characters'))

    password = "".join(random.sample(generer, longueurdumotdepasse))

    # save the generated password to the session for the current user
    if 'passwords' not in request.session:
        request.session['passwords'] = []
    request.session['passwords'].append(password)
    motdepasse = request.session.get('passwords', [])

    return render(request, 'password.html', {"passwords": password, "motdepasse": motdepasse})



