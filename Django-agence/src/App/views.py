from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from App.forms import UserForm
from App.models import Donnee, Contact


@login_required(login_url='login')
def home(request):
    product = Donnee.objects.all()
    context = {
        "produits": product,
    }
    return render(request, 'home.html', context)


def Connexion(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, '')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
        else:
            messages.error(request, "Erreur d'authentification")
    return render(request, 'login.html')


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte a été bien créer")
            return redirect('login')
        else:
            messages.error(request, form.errors)
    return render(request, 'register.html', {'form': form})


@login_required()
def deconnection(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        message = request.POST.get('message')
        com = Contact.objects.create(nom=nom, email=email, message=message)
        com.save
        return redirect('confirmation')
    return render(request, 'contact.html')


def confimation(request):
    info = Contact.objects.all()[:1]
    for item in info:
        nom = item.nom

    return render(request, 'confirmation.html', {'name': nom})
