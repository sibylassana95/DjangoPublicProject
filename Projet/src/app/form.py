from django import forms

from app.models import Produits
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Formulaire d'inscription
class UserForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'input',
        }
    ))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'input',
        }
    ))
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'input',
        }
    ))
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'input',
        }
    ))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'input',
        }
    ))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'input',
        }
    ))

    address = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-label',
        }
    ))
    number = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-label',
        }
    ))

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'address',
            'number'
        ]


# Formulaire d'ajout d'un produit
class ProductForm(forms.ModelForm):
    nom = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'input',
        }
    ))
    description = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'rows': 5,
            'cols': 10,
            'class': 'input',

        }
    ))
    prix = forms.DecimalField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'input',
        }
    ))
    stock = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'input',
        }
    ))

    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'input'}))

    class Meta:
        model = Produits
        fields = ('nom', 'description', 'prix', 'stock', 'image')


""" 
class ProductForm(forms.ModelForm):
    model = Produits
    fields = ('nom', 'description', 'prix', 'stock', 'image')

"""
