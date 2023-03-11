from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView

from app.form import ProductForm, UserForm
from app.models import Produits
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Affichage des Produits

@login_required(login_url='login')
def Produit(request):
    product = Produits.objects.all()
    if request.method == "GET":
        nom = request.GET.get('recherche')
        if nom is not None:
            product = Produits.objects.filter(nom__icontains=nom)
    context = {
        "produits": product,

    }
    return render(request, "app/produit.html", context)


# Formulaire d'inscription

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
    return render(request, 'app/register.html', {'form': form})


# Formulaire de Connexion
def connexion(request):
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
                return redirect('table')
        else:
            messages.error(request, "erreur d'authentification ")
    return render(request, 'app/login.html')


# Deconnection
@login_required()
def deconnection(request):
    logout(request)
    return redirect('login')


# Ajout d'un produit
@login_required(login_url='login')
def ProductCreate(request):
    form = ProductForm(request.POST or None, request.FILES)
    messages1 = ''
    if form.is_valid():
        form.save()
        return redirect('produit')
        messages1 = "Produit enregistrer"
    return render(request, 'app/create.html', {'form': form, 'message': messages1})


# Modification d'un produit
@login_required(login_url='login')
def ProductUpdate(request, my_id):
    obj = get_object_or_404(Produits, id=my_id)
    form = ProductForm(request.POST or None, instance=obj)
    messages1 = ''
    if form.is_valid():
        form.save()
        return redirect('table')
        messages1 = "Modification réussi!"
    return render(request, "app/update.html", {'form': form, 'message': messages1})


# Suppression d'un produit
@login_required(login_url='login')
def deleteProduct(request, my_id):
    obj = get_object_or_404(Produits, id=my_id)
    name = obj.nom
    if request.method == "POST":
        obj.delete()
        return redirect('table')

    return render(request, 'app/delete.html', {"name": name})


# Affichage des produits dans une table
@login_required(login_url='login')
def table(request):
    obj = Produits.objects.all()
    if request.method == "GET":
        nom = request.GET.get('recherche')
        if nom is not None:
            obj = Produits.objects.filter(nom__icontains=nom)

    return render(request, 'app/table.html', {'obj': obj})


""" 
def ProductCreate(request):
    message = ''
    if request.method == "POST":
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        prix = request.POST.get('prix')
        stock = request.POST.get('stock')
        image = request.POST.get('image')
        newProduit = Produits.objects.create(nom=nom, description=description, prix=prix, stock=stock, image=image)
        newProduit.save()

        message = "Enregistrement réussi!"

    return render(request, "app/create.html", {'message': message})

"""
